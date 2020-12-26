from google.cloud import bigquery
client = bigquery.Client()
hn_dataset_ref = client.dataset('chicago_crime', project='bigquery-public-data')
hn_dset = client.get_dataset(hn_dataset_ref)
print([x.table_id for x in client.list_tables(hn_dset)])