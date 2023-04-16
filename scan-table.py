#import boto3 and boto3 resource dynamodb

import boto3
dynamodb = boto3.resource('dynamodb')

#set a value and select your table name you created

table = dynamodb.Table('movies')

#scan your table for items within your table 
response = table.scan()
data = response['Items']

#use a while loop and lastevaluatedkey and exclusivestartkey to retrive table items

while 'lastevaluatedkey' in response:
    response = table.scan(exclusivestartkey=response['lastevluatedkey'])     
    data.extend(response['Items'])
    
#print to see scan results

print(data)


