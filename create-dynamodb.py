#import boto3 and boto3.resource for dynamodb

import boto3
dynamodb = boto3.resource('dynamodb')

#create dynamodb table name and keyschema

table = dynamodb.create_table(
   TableName='movies', 
   KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ], 
   
   #define attributes for you dynamodb table
   
      AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
    ],
   
   #provision your read and write capacity units 
   
    ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
    }        
)
# print table to create dynamodb table

print("Table status", table.table_status)
