import boto3
file = open('./S3_keys.txt')
access_key = file.readline().replace('\n', '')
secret_key = file.readline().replace('\n', '')
file.close()

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_key)
bucket = 'maurosbucket'

filename = './example.txt'
client.upload_file(Filename = filename, Bucket = bucket, Key = 'Example.txt')