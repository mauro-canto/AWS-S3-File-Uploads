# AWS-S3-File-Uploads
Script to upload files to an AWS S3 bucket, given its credentials provided in a separate file.

- S3_file_uploader.py: Uploads an specified file.
- S3_direct_csv_uploader.py: Directly drops a .csv from a pandas dataframe, without the needing to save it locally.

**NOTE:** They "aws_access_key_id" and the "aws_secret_access_key" are read from an external .txt file where they are contained one in each row. Such file is not added into the repository for security reasons.
