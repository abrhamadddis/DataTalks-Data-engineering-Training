"""Chess source helpers"""

from dlt.common.typing import StrAny
from dlt.sources.helpers import requests

from .settings import OFFICIAL_CHESS_API_URL
from google.cloud import storage
import pandas as pd

def get_url_with_retry(url: str) -> StrAny:
    r = requests.get(url)
    return r.json()  # type: ignore

def get_path_with_retry():
    pass
def validate_month_string():
    pass

def list_gcs_files(bucket_name, prefix):
    """List all .csv.gz files in a specific directory in GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # List files under the directory
    
    # Return only .csv.gz files
    return [blob.name for blob in blobs if blob.name.endswith(".csv.gz")]

def load_csv_from_gcs(bucket_name, file_name, chunk_size=100000):
    """Reads a CSV.GZ file from GCS in chunks and yields DataFrames."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    with blob.open("rb") as file:
        for chunk in pd.read_csv(file, compression='gzip', chunksize=chunk_size):
            yield chunk  # Yield each chunk as a DataFrame
