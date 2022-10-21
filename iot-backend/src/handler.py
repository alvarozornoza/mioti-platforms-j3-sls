import json
import logging
import os
import time
import uuid

import sys
sys.path.insert(0, 'src/vendor')
from twilio.rest import Client
import boto3

dynamodb = boto3.resource('dynamodb')

DEVICES_TABLE = os.environ['DEVICES_TABLE']
EVENTS_TABLE = os.environ['EVENTS_TABLE']
DEFAULT_NUMBER = '+34666666666'
ACCOUNT_SID = os.environ['ACCOUNT_SID']
ACCOUNT_TOKEN = os.environ['ACCOUNT_TOKEN']
TWIML_BIN = 'https://handler.twilio.com/twiml/EH31757389a99a416ea22e0237f056775f?Name'

def parseEvent(event, context):
    data = json.loads(event['body'])

    if 'deviceId' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    decodedPayload = decodePayload(data['payload'])
    createEvent(data, decodedPayload)
    device = getDevice(data['deviceId'])
    if not device:
        device = createDevice(data)
    processNotifications(device, decodedPayload)

    response = {
        "statusCode": 200,
        "body": "Message was processed correctly",
        "headers": {
            "Content-Type": "application/json"
        }
    }
    return response

def createDevice(data):
    deviceItem = {
        'deviceId': data['deviceId'],
        'name': data['deviceId'],
        'phoneNumber': DEFAULT_NUMBER,
        'createdAt': int(time.time())
    }
    devicesTable = dynamodb.Table(DEVICES_TABLE)
    devicesTable.put_item(Item=deviceItem)
    return deviceItem

def createEvent(data, decodedPayload):
    eventItem = {
        'uuid': str(uuid.uuid1()),
        'deviceId': data['deviceId'],
        'payloadRaw': data['payload'],
        'createdAt': int(time.time()),
    }
    eventItem = {**eventItem, **decodedPayload} # Juntamos eventItem y decodedPayload
    eventsTable = dynamodb.Table(EVENTS_TABLE)
    print(eventItem)
    eventsTable.put_item(Item=eventItem)

def decodePayload(raw_payload):
    decoded = dict()
    byte_array = bytearray.fromhex(raw_payload)
    i = 0
    while(i < len(byte_array)):
        channel_id = byte_array[i]
        i+=1
        channel_type = byte_array[i]
        i+=1
        # battery
        if (channel_id == 0x01 and channel_type == 0x75):
            decoded['battery'] = byte_array[i]
            i+=1
        # press state
        elif(channel_id == 0xff and channel_type == 0x2e):
            if(byte_array[i] == 0x01):
                decoded['press'] = "short"
            elif(byte_array[i] == 0x02):
                decoded['press'] = "long"
            elif(byte_array[i] == 0x03):
                decoded['press'] = "double"
            else:
                logging("unsupported")
            i+=1
    return decoded

def getDevice(deviceId):
    devicesTable = dynamodb.Table(DEVICES_TABLE)
    response = devicesTable.get_item(
        Key={
            'deviceId': deviceId
        }
    )
    if 'Item' in response:
        return response['Item']
    else:
        return dict()

def processNotifications(device, decodedPayload):
    if device['phoneNumber'] != DEFAULT_NUMBER:
        if decodedPayload['press'] == 'short':
            makeCall(device['phoneNumber'], device['name'])

def makeCall(phoneNumber, deviceName):
    client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

    client.calls.create(
        to = phoneNumber,
        from_ = '+12137724396',
        url = TWIML_BIN + deviceName
    )