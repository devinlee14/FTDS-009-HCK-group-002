import pandas as pd

def clean(df_path: str):
   """
   Perform a series of data cleaning operations on a CSV file.

   The function reads the file into a pandas DataFrame, processes it, 
   and saves the cleaned data back to a CSV file. It handles missing values, 
   formats and normalizes various columns, and converts data types as necessary.

   Parameters:
   - df_path (str): The file path of the CSV file to be cleaned.

   Operations Performed:
   1. Drop rows with any missing values.
   2. Convert all column names to lowercase and replace spaces with underscores.
   3. Convert all string data in the DataFrame to lowercase.
   4. Format 'sentiment_polarity' and 'sentiment_subjectivity' to round to two decimal places.
   5. - Remove dollar signs and convert 'price' column to float.
      - Remove '+' and ',' characters and convert 'installs' column to integer.
      - Convert 'last_updated' column to datetime format.
   6. Drop duplicates.
   7. - Split 'Genres' column values into lists, separating genres using ';'.
      - Normalize the 'Genres' column by converting all genres to lowercase.
   8. Save the cleaned DataFrame to '/opt/airflow/data_clean/data_clean.csv'.

   Usage Example:
   >>> clean('/path/to/your/input_data.csv')
   This processes the file at the specified path and outputs the cleaned data to 
   '/opt/airflow/data_clean/data_clean.csv'.
   """
   # Fetch the csv file into a dataframe
   df = pd.read_csv(df_path)

   # Drop missing values
   df = df.dropna()

   # Convert column names to lowercase
   df.columns = df.columns.str.lower()

   # Replace column names space with underscore (_) 
   df.columns = df.columns.str.replace(' ', '_')

   # Convert all object columns to lowercase
   df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

   # Format numbers to two decimal places
   df[['sentiment_polarity', 'sentiment_subjectivity']] = df[['sentiment_polarity', 'sentiment_subjectivity']].round(2)

   # Replace and convert datatype
   df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
   df['installs'] = df['installs'].str.replace('+', '').str.replace(',', '').astype(int)
   df['last_updated'] = pd.to_datetime(df['last_updated'])

   # Drop duplicates
   df = df.drop_duplicates()

   # Convert genres to list and separate the genres by ';'
   df['genres'] = df['genres'].apply(lambda x: x.split(';'))

   # Save the file locally
   df.to_csv('/opt/airflow/data_clean/data_clean.csv', index=False) 