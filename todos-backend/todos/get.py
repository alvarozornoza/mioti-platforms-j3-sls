import os
import json
import sys

sys.path.append('../')
from lib import decimalencoder

import boto3
dynamodb = boto3.resource('dynamodb')

def getOne(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'], cls=decimalencoder.DecimalEncoder),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response

def getAll(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder),
        "headers": {
            "Content-Type": "application/json"
        }
    }

    return response