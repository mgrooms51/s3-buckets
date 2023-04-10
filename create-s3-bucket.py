#!/usr/bin/env python3.7

# In the terminal use pip3 install awscli to install aws command line 

# In terminal use pip3 install boto3 to install boto3

import boto3

aws_resource=boto3.resource("s3")

bucket=aws_resource.Bucket("mellygs3")

response = bucket.create(
    #This code creates a public s3 bucket
    
    ACL='public-read',
    
 #create bucket configuration are not used in us-east-1
)
print(response)