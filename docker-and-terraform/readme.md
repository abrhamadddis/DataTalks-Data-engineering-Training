# NYC Taxi Data Pipeline

## Project Overview

This project is designed to process and analyze NYC taxi trip data. It provides a ETL pipeline for data ingestion, transformation, and analysis using containerized environments and SQL queries

## Directory Structure

````

├── docker-compose.yaml                      # Docker Compose configuration file
├── Dockerfile                               # Dockerfile to set up the environment
├── homework                                 # SQL queries for data analysis
├── ingest_data.py                           # Python script for data ingestion
├── notebooks                                # Jupyter notebooks for exploratory analysis
├── requirements.txt                         # Required Python dependencies


## Setup Instructions
### Prerequisites
- Install Docker and Docker Compose
- Install Python 3.x and required dependencies

### Running the Project
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
````

2. Build and start the Docker containers:
   ```sh
   docker-compose up --build
   ```
3. Run the ingestion script to load data:
   ```sh
   python ingest_data.py
   ```
4. Execute SQL queries from the `homework` directory to analyze the data.
5. Open Jupyter notebooks for further exploration:
   ```sh
   jupyter notebook
   ```

## Key Features

- data ingestion and transformation
- SQL-based data processing and analysis
- exploration through Jupyter Notebooks
- Containerized deployment with Docker
