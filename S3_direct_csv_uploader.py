import pandas as pd
import boto3
file = open('./S3_keys.txt')
access_key = file.readline().replace('\n', '')
secret_key = file.readline().replace('\n', '')
file.close()

df = pd.DataFrame()
df['Day'] = ['01/01/1900', '01/02/1900', '01/03/1900']
df['Value'] = [10, 18, 15]
csv_string = df.to_csv(index = False)

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_key)
bucket = 'maurosbucket'

client.put_object(Body = csv_string, Bucket = bucket, Key = 'CSV_Example.csv')