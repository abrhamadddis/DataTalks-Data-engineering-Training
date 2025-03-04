import dlt
from chess.helpers import list_gcs_files, load_csv_from_gcs

# Define your GCS bucket name
BUCKET_NAME = "ny_taxi_dataeng_week_four"

# Mapping directories to BigQuery tables
GCS_DIRECTORIES = {
    "green/": "green_taxi",
    "yellow/": "yellow_taxi",
    "fhv/": "fhv_taxi"
}

def load_all_taxi_data():
    """Loads all taxi data from GCS into BigQuery in chunks."""
    
    # Define the pipeline
    pipeline = dlt.pipeline(
        pipeline_name="ny_taxi_pipeline",
        destination="bigquery",
        dataset_name="ny_taxi_data",
    )

    for directory, table_name in GCS_DIRECTORIES.items():
        # List all .csv.gz files in the directory
        files = list_gcs_files(BUCKET_NAME, directory)

        for file_name in files:
            print(f"Processing file: {file_name} into {table_name}...")

            # Process each file in chunks
            for chunk in load_csv_from_gcs(BUCKET_NAME, file_name):
                print(f"Loading {len(chunk)} rows into {table_name}...")
                
                # Load each chunk into BigQuery
                info = pipeline.run(chunk, table_name=table_name)
                print(info)

if __name__ == "__main__":
    load_all_taxi_data()
