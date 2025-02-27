import os
import urllib.request
import io
from concurrent.futures import ThreadPoolExecutor
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

# Change this to your bucket name
BUCKET_NAME = os.getenv("BUCKET_NAME")
CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE")

client = storage.Client.from_service_account_json(CREDENTIALS_FILE)

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download"
DIRECTORIES = ["yellow", "fhv"]
YEARS = [2019, 2020, 2021]
MONTHS = [f"{i:02d}" for i in range(1, 13)]

bucket = client.bucket(BUCKET_NAME)

def upload_to_gcs_from_url(url, blob_name):
    try:
        print(f"Uploading {url} to gs://{BUCKET_NAME}/{blob_name}...")
        blob = bucket.blob(blob_name)
        with urllib.request.urlopen(url) as response:
            # Stream the response content in chunks
            with blob.open("wb") as f:
                while True:
                    chunk = response.read(1024 * 1024)  # Read in 1MB chunks
                    if not chunk:
                        break
                    f.write(chunk)
        print(f"Uploaded: gs://{BUCKET_NAME}/{blob_name}")
    except Exception as e:
        print(f"Failed to upload {url} to GCS: {e}")

def process_file(directory, year, month):
    if year == 2021 and int(month) > 7:
        return  # Skip months after July 2021 for green and yellow directories

    file_name = f"{directory}_tripdata_{year}-{month}.csv.gz"
    url = f"{BASE_URL}/{directory}/{file_name}"
    blob_name = f"{directory}/{file_name}"
    upload_to_gcs_from_url(url, blob_name)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Process files
        executor.map(
            lambda params: process_file(*params),
            [(directory, year, month) for directory in DIRECTORIES for year in YEARS for month in MONTHS]
        )

    print("All files processed and uploaded to GCS.")