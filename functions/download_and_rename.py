from airflow.providers.amazon.aws.hooks.s3 import S3Hook 
import os

def download_from_s3(key: str, bucket_name: str, local_path: str, new_file_name: str) -> str:
    """
    This function downloads the file from the S3 bucket and renames the file with the arguments:
    1. key: path/to/file.csv
    2. bucket_name: Name of bucket
    3. local_path: Path where the file is downloaded to
    4. new_file_name: Name of the new file
    and returns the new file name
    """
    # S3 Hook
    hook = S3Hook('s3_conn') 

    if not os.path.exists(local_path):
        os.makedirs(local_path)
    
    # Download file
    file_name = hook.download_file(key=key, bucket_name=bucket_name, local_path=local_path) 

    # Path to downloaded file
    raw_file_path = os.path.join(local_path, file_name)

    # Path to renamed file
    renamed_file_path = os.path.join(local_path, new_file_name)

    # Rename file
    os.rename(raw_file_path, renamed_file_path)

    return renamed_file_path