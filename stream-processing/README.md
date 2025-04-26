# NYC Taxi Data Stream Processing

## Project Overview

This project implements real-time stream processing for NYC taxi data using Apache Flink. It provides a scalable and fault-tolerant solution for processing taxi trip data in real-time, enabling immediate insights and analytics.

## Directory Structure

```
├── docker-compose.yml                  # Docker Compose configuration for services
├── Dockerfile.flink                    # Dockerfile for Apache Flink setup
├── requirements.txt                    # Python dependencies
├── src/                               # Source code for stream processing
└── keys/                              # Security keys and credentials
```

## Setup Instructions

### Prerequisites
- Docker and Docker Compose
- Python 3.x
- Required Python packages (install using pip):
  ```sh
  pip install -r requirements.txt
  ```

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

3. The stream processing pipeline will automatically start processing incoming taxi data.

## Key Features

- Real-time data processing using Apache Flink
- Scalable and fault-tolerant architecture
- Containerized deployment with Docker
- Real-time analytics and insights
- Integration with existing data pipeline

## Stream Processing Workflow

1. Data Ingestion: Real-time taxi data is ingested into the system
2. Stream Processing: Apache Flink processes the data streams
3. Analytics: Real-time analytics are performed on the streaming data
4. Output: Processed data is stored or forwarded for further analysis

## Contributing

Feel free to contribute to this project by:
- Adding new stream processing jobs
- Improving existing analytics
- Enhancing documentation
- Adding new features 