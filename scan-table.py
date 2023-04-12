import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('movies')

response = table.scan()

data = response['Items']

while 'lastevaluatedkey' in response:
    response = table.scan(exclusivestartkey=response['lastevluatedkey'])
    
    data.extend(response['Items'])


print(data)


