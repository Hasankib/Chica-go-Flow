from google.cloud import bigquery

client = bigquery.Client()
hn_dataset_ref = client.dataset('chicago_crime', project='bigquery-public-data')
hn_dset = client.get_dataset(hn_dataset_ref)
dictionary = {}

for i in range (1,78):
    dictionary[i] = 0

for x in client.list_tables(hn_dset):
    for y in (client.list_rows(x)):
        if(type(y['community_area'])==int):
            if((y['community_area']<=77 and y['community_area']>=1)):
                dictionary[y['community_area']] += 1

file1 = open("dataset.txt","w")
file1.write(str(dictionary))
file1.close()