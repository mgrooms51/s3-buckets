import boto3
#how to list s3 bucket objects
s3_resource=boto3.client("s3")

objects=s3_resource.list_objects(Bucket="mellygs3")["Contents"]

for object in objects:
    print(object["Key"])

