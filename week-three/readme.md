# NYC Taxi Data-warehouse - Week Three

## Project Overview

This project ingests, stores, and queries NYC Yellow Taxi trip data. The pipeline downloads the data, uploads it to Google Cloud Storage (GCS), and creates tables in BigQuery for analysis.

## Directory Structure

```sh
.
├── homework/                                # SQL queries for analysis
│   └── answer.sql
├── load_yellow_taxi_data.py                 # Script to download and upload data to GCS
```

## Data Ingestion and Processing

- Automates downloading and uploading Yellow Taxi trip data to GCS.
- Uses a multi-threaded approach for efficiency.

## Key Features

- Automated data processing
- Cloud storage integration
- Optimized querying with BigQuery
- Multi-threaded execution for efficiency

This pipeline streamlines NYC Taxi data processing for large-scale analysis using cloud resources.

