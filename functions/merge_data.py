import pandas as pd

def merge(df1_path: str, df2_path: str):
    """
    Merge two CSV files into a single DataFrame and save the result.

    This function loads two datasets from the specified CSV file paths, 
    merges them into a single DataFrame using an inner join on the 'App' column,
    and then saves the merged DataFrame to a CSV file.

    Parameters:
    - df1_path (str): File path for the first CSV file.
    - df2_path (str): File path for the second CSV file.

    Usage Example:
    >>> merge('/path/to/first_dataset.csv', '/path/to/second_dataset.csv')
    This will load the datasets, merge them, and save the merged data to
    '/opt/airflow/data/data_merged_raw.csv'.
    """
    # Load the two datasets
    df1 = pd.read_csv(df1_path)
    df2 = pd.read_csv(df2_path)

    # Merge the two dataframes
    df = pd.merge(df1, df2, on='App', how='inner')

    # Save the merged dataframe
    df.to_csv('/opt/airflow/data/data_merged_raw.csv', index=False)