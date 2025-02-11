
### Files and Directories

- **docker-compose.yml**: Docker Compose configuration file for setting up the necessary services.
- **flows/**: Contains YAML files for various data engineering workflows.
  - **gcp_dbt.yaml**: Configuration for DBT (Data Build Tool) on GCP.
  - **gcp_kv.yaml**: Key-value store configuration for GCP.
  - **gcp_setup.yaml**: Setup configuration for GCP resources.
  - **gcp_taxi.yaml**: Workflow for processing taxi data on GCP.
  - **postgres_dbt.yaml**: Configuration for DBT on PostgreSQL.
  - **postgres_taxi_scheduled.yaml**: Scheduled workflow for processing taxi data on PostgreSQL.
  - **postgres_taxi.yaml**: Workflow for processing taxi data on PostgreSQL.
- **homework/**: Contains YAML files for various homework tasks.
  - **file_size.yaml**: Task for calculating file size.
  - **number_of_rows.yaml**: Task for counting the number of rows.
  - **rendered_value.yaml**: Task for rendering values.

## Environment Variables

Ensure you have a `.env` file in the root directory with the following content:

```plaintext
GCP_PROJECT_ID=your_project_id
GCP_LOCATION=your_location
GCP_BUCKET_NAME=your_bucket_name
GCP_DATASET=your_dataset
GCP_CREDS=your_service_account_credentials
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password