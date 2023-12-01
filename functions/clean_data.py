import pandas as pd

def clean(df_path: str):
    df = pd.read_csv(df_path)
    # Handling Missing Value
    df = df.dropna()

    # Convert genre to list and separate the genres by ; 
    df['Genres'] = df['Genres'].apply(lambda x: x.split(';'))
    
    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace column names space with underscore (_) 
    df.columns = df.columns.str.replace(' ', '_')



    # Convert to lowercase
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # Format numbers to two decimal places
    df[['sentiment_polarity', 'sentiment_subjectivity']] = df[['sentiment_polarity', 'sentiment_subjectivity']].round(2)

    # Replace and convert datatype
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['installs'] = df['installs'].str.replace('+', '').str.replace(',', '').astype(int)
    df['last_updated'] = pd.to_datetime(df['last_updated'])

    df.to_csv('/opt/airflow/data_clean/data_clean.csv', index=False) 