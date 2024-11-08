from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import json

# Function to fetch data from OpenWeatherMap API
def fetch_weather_data():
    api_key = '643317a91e07640cfe015328345dc5b5'  # Replace with your OpenWeatherMap API key
    city = 'London'  # Replace with your city
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    response = requests.get(url)
    weather_data = response.json()

    # Store data in a JSON file locally
    with open('/path/to/save/weather_data.json', 'w') as f:
        json.dump(weather_data, f)

# Default arguments for the DAG
default_args = {
    'owner': 'student',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG('weather_data_ingestion', default_args=default_args, schedule_interval='@hourly')

# Create a task to fetch data
fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)
