# NYC Taxi Data Analytics Engineering

## Project Overview

This project focuses on analytics engineering for the NYC taxi data pipeline. It provides tools and workflows for data analysis, transformation, and visualization using modern analytics engineering practices.

## Directory Structure

```
├── download_data.sh                    # Script to download required datasets
├── notebook/                           # Jupyter notebooks for data analysis
│   ├── data_analysis.ipynb            # Main analysis notebook
│   ├── data_visualization.ipynb       # Visualization notebook
│   └── data_transformation.ipynb      # Data transformation notebook
```

## Setup Instructions

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required Python packages (install using pip):
  ```sh
  pip install pandas numpy matplotlib seaborn jupyter
  ```

### Running the Project
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Download the required data:
   ```sh
   ./download_data.sh
   ```

3. Start Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

4. Open and run the notebooks in the `notebook/` directory to perform analysis.

## Key Features

- Data analysis and visualization
- Statistical analysis of taxi trips
- Data transformation and cleaning
- Interactive data exploration
- Automated data downloading

## Data Analysis Workflow

1. Data Ingestion: Use `download_data.sh` to get the required datasets
2. Data Cleaning: Transform and clean the data using the transformation notebook
3. Analysis: Perform statistical analysis and create visualizations
4. Reporting: Generate insights and reports from the analysis

## Contributing

Feel free to contribute to this project by:
- Adding new analysis notebooks
- Improving existing visualizations
- Adding new data transformation scripts
- Enhancing documentation
