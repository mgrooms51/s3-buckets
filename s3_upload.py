import boto3
#how to upload single file
s3_resource=boto3.client("s3")

s3_resource.upload_file(
    Filename="s3_upload.py",
    Bucket="mellygs3",
    Key="test_s3_upload.py")
#how to upload multiple files
import os
import glob
cwd=os.getcwd()
cwd=cwd+"/s3-buckets/"
files=glob.glob(cwd+"*.py")

for file in files:
    s3_resource.upload_file(
    Filename=file,
    Bucket="mellygs3",
    Key=file.split("/")[-1])
    

    