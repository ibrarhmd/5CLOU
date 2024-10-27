# Building a unified data platform for real-time event analysis

## Project introduction

In today’s data-driven world, organizations are increasingly relying on **data platforms** to collect, manage, and analyze data in real-time.<br />
A **data platform** is an integrated solution that brings together various tools and services to ingest, process, store, and visualize data.<br />
It allows for scalable data handling and supports real-time analytics, enabling businesses to make data-driven decisions quickly and effectively.

In this project, you will design and implement a **real-time data platform** using **Microsoft Azure Fabric** services.
Your platform will ingest live or periodically updated data from any **open data source** of your choice, process it in real-time, and display insights using interactive dashboards.

This project will provide hands-on experience with key components of **Azure Fabric**: **Data Factory** for data ingestion, **Synapse Analytics** for real-time processing, and **Power BI** for visualization.

Additionally, you are encouraged to use **Python** for any data transformation, processing, or automation tasks within **Synapse Analytics** or the data pipeline.

---

## Objective

- Build a data platform that can **ingest**, **process**, and **visualize** real-time data using Microsoft Azure services.
- Choose a relevant **open data source** (e.g., sports events, stock market feeds, weather data) and design a system to provide real-time insights.
- Use **Python** when necessary for data processing or automation within the project.

---

## Prelude

### How to get free Credits with GitHub student developer pack

Before diving into the project, students can take advantage of the **GitHub Student Developer Pack**, which offers free credits 
for various cloud services, including Microsoft Azure. 

By signing up for the pack, you'll gain access to tools like Azure, AWS, and Google Cloud at no cost, allowing you to experiment 
with real cloud infrastructure. To get started, visit the [GitHub Student Developer Pack page](https://education.github.com/pack), 
verify your student status, and claim your benefits. This will give you free access to cloud resources that can be used for projects 
like this one, enabling you to work on cloud-based solutions without worrying about costs.

### About Azure Services and local alternatives

This project is designed to teach you how to build real-time data pipelines using **Azure services** like **Azure Data Factory**, 
**Synapse Analytics**, and **Power BI**. However, due to potential limitations in accessing cloud credits or services, we’ve provided 
local alternatives like **Apache Airflow**, **Pandas**, and **Jupyter Notebooks**. 

Even though these are local tools, the concepts, techniques, and workflows remain the same.
The essence of learning—building robust data ingestion pipelines, processing data, and visualizing insights—is fully preserved. 
Mastering these local tools will give you the foundation needed

---

## Steps to complete the project

### Step 1: Selecting an open data source

Begin by selecting an **open data source** that provides real-time or frequently updated data. You can use APIs or datasets from platforms like:
- **Paris 2024 data** ([Paris Open Data](https://data.paris2024.org/explore/?sort=modified))
- **Stock Market Feeds** (e.g., Alpha Vantage, Yahoo Finance)
- **Weather Data** (e.g., OpenWeatherMap)
- Etc.

Make sure to choose a source that updates frequently so you can simulate real-time analysis.

### Step 2: Setting up the data ingestion pipeline

> [!IMPORTANT]
> If you have credits for Azure services, you can proceed with the following steps.

You will use **Azure Data Factory** to ingest the selected data. Data Factory allows you to automate the extraction of data from various sources, including REST APIs, blob storage, or databases.

1. **Create an Azure Data Factory**:
    - Go to the **Azure Portal** and search for **Data Factory**.
    - Create a new **Data Factory** instance.
    - Set up a **pipeline** to periodically ingest data from your chosen open data source.

2. **Ingest Data**:
    - Use **Copy Data activity** in **Data Factory** to ingest data from your selected API or data file.
    - Configure the frequency of data ingestion (e.g., every minute or every hour).
    - Store the ingested data in **Azure Blob Storage** or directly into **Azure Synapse Analytics** for processing.

**Output**: A fully operational data ingestion pipeline that collects data from the chosen source in real-time and stores it in a cloud-based data store.

> [!IMPORTANT]
> Otherwise, you can simulate the data ingestion and processing locally.

Instead of using Azure Data Factory, students can set up a data ingestion pipeline locally using Python and Apache Airflow for orchestration.

1. **Set up Apache Airflow locally**:
   - Install [Airflow](https://airflow.apache.org/) on your local machine (via Docker, or Python's pip).
   - Write a DAG (Directed Acyclic Graph) to automate the extraction of data from the selected APIs or sources.

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

def fetch_data():
    response = requests.get("<API URL>")
    with open('/path/to/data.csv', 'w') as file:
        file.write(response.text)

default_args = {
    'owner': 'student',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_ingestion', default_args=default_args, schedule_interval='@hourly')

fetch_data_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    dag=dag,
)
```

2. **Ingest Data**:
   - Schedule the DAG to run periodically and fetch the data (e.g., every hour or day).
   - Store the ingested data locally in CSV or in SQLite.

**Output**: A data ingestion pipeline managed locally using Airflow, which collects data from the open source in real time.

### Step 3: Real-time data processing with Synapse Analytics (Use Python)

> [!IMPORTANT]
> If you have credits for Azure services, you can proceed with the following steps.

Now that you have the data, the next step is to process it in real-time using **Azure Synapse Analytics**. You will use **Python** for data transformations or analytics within Synapse.

1. **Set up Synapse Workspace**:
    - In the **Azure Portal**, create a **Synapse Analytics Workspace**.
    - Link your **Azure Data Lake** or **Blob Storage** where the ingested data is stored.

2. **Create a Spark Pool or SQL Pool**:
    - Use **Apache Spark** (Python notebooks) or **SQL Pool** to perform real-time analysis on the ingested data.
    - Write transformation queries that clean and format the data for visualization.

3. **Process the Data with Python**:
    - If using **Spark**, you can use **Python** to write data transformation scripts.
    - Example Python code:
      ```python
      from pyspark.sql import SparkSession
 
      spark = SparkSession.builder.appName("RealTimeDataProcessing").getOrCreate()
 
      # Load the data from storage
      df = spark.read.csv("wasbs://<container>@<storage_account>.blob.core.windows.net/<file.csv>")
 
      # Perform transformations
      df_filtered = df.filter(df['column'] > 100)  # Example transformation
 
      df_filtered.show()
      ```

**Output**: Real-time data processing pipeline using Python within Synapse Analytics that transforms raw data into meaningful insights, ready for visualization.

> [!IMPORTANT]
> Otherwise, you can process data locally using Pandas

Now that you have the data, the next step is to process them locally using Python with the [Pandas](https://pandas.pydata.org/) library.

1. **Install Pandas**:
   - Install Pandas via pip (`pip install pandas`). 

2. **Write transformation code**: 
   - Load the ingested data (from CSV or database) and perform transformations using Pandas.

Example transformation script:

```python
import pandas as pd

# Load data from local CSV
df = pd.read_csv('/path/to/data.csv')

# Perform data cleaning or filtering
df_cleaned = df[df['value'] > 100]  # Example filtering based on some column

# Save the transformed data
df_cleaned.to_csv('/path/to/cleaned_data.csv', index=False)
```

**Output**: Data processing and transformation pipeline using Python Pandas, ready for visualization.

### Step 4: Visualizing data with Power BI

> [!IMPORTANT]
> If you have credits for Azure services, you can proceed with the following steps.

Once the data is processed, it's time to create an **interactive dashboard** using **Power BI**.

1. **Connect Power BI to Synapse Analytics**:
    - Open **Power BI** and connect it to the **Azure Synapse Analytics Workspace**.

2. **Build interactive reports**:
    - Use **Power BI Desktop** to create interactive reports and dashboards that visualize key metrics from the data.
    - Examples include live event statistics, stock price movements, or weather pattern visualizations.

3. **Real-time dashboard**:
    - Enable **real-time refresh** in Power BI so that your dashboards update automatically as new data is processed.

**Output**: A live, interactive Power BI dashboard that showcases real-time insights based on the ingested and processed data.

> [!IMPORTANT]
> Otherwise, you can visualizing data locally with Tableau public or jupyter notebooks

Instead of Power BI, we'll use [Tableau Public](https://public.tableau.com/app/discover) or [Jupyter Notebooks](https://jupyter.org/) for visualization.

1. **Jupyter Notebooks**:
   - Install Jupyter using pip (`pip install jupyter`). 
   - Use `matplotlib` or `plotly` for data visualization in notebooks.

Exemples:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load transformed data
df_cleaned = pd.read_csv('/path/to/cleaned_data.csv')

# Plot the data
df_cleaned.plot(x='date', y='value', kind='line')
plt.show()
```

2. **Tableau Public**:
   - Export the cleaned data from Pandas to CSV and import it into Tableau Public. 
   - Build interactive dashboards using the provided data and publish them online.

**Output**: Real-time visualizations using Jupyter Notebook or Tableau Public with the ability to refresh data frequently.

---

## Bonus: Infrastructure as Code (IaC) with Terraform

As a bonus, you can implement **Infrastructure as Code** (IaC) using **Terraform** to automate the deployment of your Azure resources.<br />
This includes deploying **Azure Data Factory**, **Synapse Analytics**, and **Power BI** components.

1. **Set up Terraform**:
    - Use the **Microsoft Fabric Terraform provider**: [Terraform Azure Fabric Provider](https://registry.terraform.io/providers/microsoft/fabric/latest/docs).

2. **Write Terraform configuration**:
    - Define your infrastructure in a `.tf` file, including the deployment of Data Factory, Synapse Analytics, and other resources needed for your data platform.

3. **Deploy the infrastructure**:
    - Run Terraform commands to provision the Azure resources automatically.

**Example Terraform snippet**:
```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_synapse_workspace" "example" {
  name                = "synapse-workspace"
  resource_group_name = "example-resources"
  location            = "West Europe"
}

resource "azurerm_synapse_spark_pool" "example" {
  name                 = "synapse-spark-pool"
  synapse_workspace_id = azurerm_synapse_workspace.example.id
  node_size_family     = "MemoryOptimized"
  node_size            = "Small"
}
