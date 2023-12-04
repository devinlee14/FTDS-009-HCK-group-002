from airflow import DAG
import datetime as dt
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from functions.download_and_rename import download_from_s3
from functions.merge_data import merge
from functions.clean_data import clean
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator

default_args = {
    'owner': 'data_engineer',
    'start_date': dt.datetime(2023, 12, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=3),
    'catchup': False
}

with DAG('process_data',
         default_args=default_args,
         schedule_interval=None
         ) as dag:
    
    # Create directory
    create_dir = BashOperator(
        task_id='create_dir',
        bash_command='mkdir -p /opt/airflow/data_clean'
    )
    
    # Fetch the play store data
    play_store = PythonOperator(
        task_id='play_store',
        python_callable=download_from_s3,
        op_kwargs={
            'key': 'raw_data/googleplaystore.csv',
            'bucket_name': 'hck-009-group-2',
            'local_path': '/opt/airflow/data/',
            'new_file_name': 'google_play_store.csv'
        }
    )

    # Fetch the user review data
    user_review = PythonOperator(
        task_id='user_review',
        python_callable=download_from_s3,
        op_kwargs={
            'key': 'raw_data/googleplaystore_user_reviews.csv',
            'bucket_name': 'hck-009-group-2',
            'local_path': '/opt/airflow/data/',
            'new_file_name': 'user_reviews.csv'
        }
    )

    # Merge the two data
    join_data = PythonOperator(
        task_id='merge_data',
        python_callable=merge,
        op_kwargs={
            'df1_path': '/opt/airflow/data/google_play_store.csv',
            'df2_path': '/opt/airflow/data/user_reviews.csv'
        }
    )

    # Clean data
    clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=clean,
        op_kwargs={
            'df_path': '/opt/airflow/data/data_merged_raw.csv'
        }
    )

    # Upload to bucket
    upload_to_s3 = LocalFilesystemToS3Operator(
        task_id='upload_to_s3',
        filename='/opt/airflow/data_clean/data_clean.csv',
        dest_key='clean_data/data_clean.csv',
        dest_bucket='hck-009-group-2',
        replace=True, 
        aws_conn_id='s3-conn'
    )

    create_dir >> [play_store, user_review] >> join_data >> clean_data >> upload_to_s3