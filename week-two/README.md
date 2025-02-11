# NYC Taxi Data Pipeline - Week Two

## Project Overview
This phase of the project extends the NYC Taxi Data Pipeline by integrating workflow orchestration using Kestra. Kestra is an open-source, event-driven orchestration platform that simplifies building both scheduled and event-driven workflows. By adopting Infrastructure as Code practices for data and process orchestration, Kestra enables structured workflows for data ingestion, transformation, and analysis using YAML-based configurations and containerized execution.

## Directory Structure
```sh
├── docker-compose.yml                        # Docker Compose configuration file for setting up services  
├── flows/                                    # Contains YAML files for various data engineering workflows  
│   ├── gcp_dbt.yaml                          # Configuration for DBT (Data Build Tool) on GCP  
│   ├── gcp_kv.yaml                           # Key-value store configuration for GCP  
│   ├── gcp_setup.yaml                        # Setup configuration for GCP resources  
│   ├── gcp_taxi.yaml                         # Workflow for processing taxi data on GCP  
│   ├── postgres_dbt.yaml                     # Configuration for DBT on PostgreSQL  
│   ├── postgres_taxi_scheduled.yaml          # Scheduled workflow for processing taxi data on PostgreSQL  
│   ├── postgres_taxi.yaml                    # Workflow for processing taxi data on PostgreSQL  
├── homework/                                 # Contains YAML files for various homework tasks  
│   ├── file_size.yaml                        # Task for calculating file size  
│   ├── number_of_rows.yaml                   # Task for counting the number of rows  
│   ├── rendered_value.yaml                   # Task for rendering values  
```
## Environment Variables
Ensure you have a `.env` file in the root directory with the following content:

```sh
GCP_PROJECT_ID=your_project_id  
GCP_LOCATION=your_location  
GCP_BUCKET_NAME=your_bucket_name  
GCP_DATASET=your_dataset  
GCP_CREDS=your_service_account_credentials  
DB_USERNAME=your_db_username  
DB_PASSWORD=your_db_password  
```

## Setup Instructions

### Prerequisites
- Install Docker and Docker Compose
- Ensure you have access to GCP and proper credentials configured

### Running the Project
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Build and start the Docker containers:
   ```sh
   docker-compose up --build
   ```
3. Execute workflows based on required tasks:
   - Run a workflow from the `flows/` directory:
     ```sh
     prefect deployment run <workflow-file>
     ```
   - Execute SQL-based transformations:
     ```sh
     dbt run
     ```
4. Verify processed data in GCP or PostgreSQL as per the configured workflows.

## Key Features
- Automated workflow execution for data processing
- GCP and PostgreSQL-based ETL workflows
- Configuration-driven task execution using YAML files
- Secure handling of credentials via environment variables
- Containerized deployment with Docker

This phase enhances the scalability and automation of the data pipeline, enabling efficient data processing and analysis.

