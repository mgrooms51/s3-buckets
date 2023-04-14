import boto3

s3_resource=boto3.client("s3")
#how to delete a single object
s3_resource.delete_object(Bucket='mellygs3',
      Key='s3_upload.py')
      
      #how to delete multiple objects
import os
import glob
#find all bucket objects
objects=s3_resource.list_objects(Bucket="mellygs3")["Contents"]

for object in objects:
    s3_resource.delete_object(Bucket='mellygs3',

    Key=object["Key"])
     
