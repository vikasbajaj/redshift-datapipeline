#!/usr/bin/env python3

import boto3
import datetime
import json

client = boto3.client('events')
response = client.put_events(
    Entries=[
        {
            'Source': 'com.aws.orders',
            'DetailType': 'NewOrder',
            'Detail': json.dumps({'category': 'lab-supplies', 'value': 415, 'location': 'us-west-2'}),
            'EventBusName': 'arn:aws:events:us-west-2:902505770441:event-bus/Orders'
        },
    ]
)
print(response['Entries'])