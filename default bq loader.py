#This script assumes that you have a CSV file named your_csv_file.csv and a Google Cloud project with a service account 
#that has the proper permissions to write to BigQuery. 
#You'll also need to set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account's 
#credentials JSON file.

#Note that this script loads the entire CSV file into memory, 
#so it may not be suitable for very large files. 
#In that case, you could use the BigQuery API's load_table_from_file method 
#or the bq command-line tool to load the data in chunks.


import csv
import os
from google.cloud import bigquery

# Set environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/credentials.json'

# Create a client object
client = bigquery.Client()

# Define the dataset and table you want to upload to
dataset_id = 'your_dataset_id'
table_id = 'your_table_id'
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

# Load the CSV file
with open('your_csv_file.csv', 'rb') as f:
    reader = csv.reader(f)
    header = next(reader) # skip the first row (header)
    rows = [row for row in reader]

# Convert the rows to BigQuery insert data format
data = [{header[i]:row[i] for i in range(len(header))} for row in rows]

# Upload the data to BigQuery
errors = client.insert_rows(table_ref, data)
if not errors:
    print('Data loaded to BigQuery successfully!')
else:
    print('Errors:')
    for error in errors:
        print(error)


