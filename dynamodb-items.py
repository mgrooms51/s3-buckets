#import boto3 and boto3 resource for dynamodb 

import boto3
dynamodb = boto3.resource('dynamodb')

#create table items use .put_item to add items to the table 

table = dynamodb.Table('movies')
table.put_item(
    Item={
        'id': 1,
        'name': 'Life',
        'genre': 'drama/comedy'
    } 
)
table.put_item(
    Item={
        'id': 2,
        'name': 'bad-boys',
        'genre': 'action/comedy'
    } 
)
table.put_item(
    Item={
        'id': 3,
        'name': 'blue-streak',
        'genre': 'comedy/crime'
    } 
)
table.put_item(
    Item={
        'id': 4,
        'name': 'Thin-line',
        'genre': 'romance/comedy'
    } 
)
table.put_item(
    Item={
        'id': 5,
        'name': 'house-party',
        'genre': 'comedy/romance'
    } 
)
table.put_item(
    Item={
        'id': 6,
        'name': 'wild-hogs',
        'genre': 'comedy/adventure'
    } 
)
table.put_item(
    Item={
        'id': 7,
        'name': 'you-so-crazy',
        'genre': 'comedy/stand-up'
    } 
)
table.put_item(
    Item={
        'id': 8,
        'name': 'big-mommas-house',
        'genre': 'comedy'
    } 
)
table.put_item(
    Item={
        'id': 9,
        'name': 'national-security',
        'genre': 'action/comedy'
    } 
)
table.put_item(
    Item={
        'id': 10,
        'name': 'nothing-to-lose',
        'genre': 'action/comedy'
    } 
)
table.put_item(
    Item={
        'id': 11,
        'name': 'rebound',
        'genre': 'comedy/sport'
    } 
)
table.put_item(
    Item={
        'id': 12,
        'name': 'black-knight',
        'genre': 'comedy/adventure'
    } 
)
