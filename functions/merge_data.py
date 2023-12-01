import pandas as pd

def merge(df1_path, df2_path):
    # Load the two datas
    df1 = pd.read_csv(df1_path)
    df2 = pd.read_csv(df2_path)

    # Merge the two datas
    df = pd.merge(df1, df2, on='App', how='inner')

    # Save the merged data
    df.to_csv('/opt/airflow/data/data_merged_raw.csv', index=False)