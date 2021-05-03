import json
import boto3
import uuid
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Rating')

def lambda_handler(event, context):
   
    finalObj={}
    
    finalObj['rate'] = event['rate']
    finalObj['channel'] =  event['channel']
    finalObj['uid'] = str(uuid.uuid4())
    finalObj['createdTime'] = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    response = table.put_item(Item=finalObj)
   
    return {
        'statusCode': 200,
        "message":"data inserted Successfully"
       
    }
