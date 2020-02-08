from datetime import datetime

import boto3
from chalice import Chalice


app = Chalice(app_name='foaas')


@app.route('/')
def index():
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')
    table = dynamodb.Table('Fuck_off')

    response = table.scan(ProjectionExpression='message')
    messages = [message.get('message') for message in response.get("Items")]

    return {
        'status': 200,
        'message': messages,
    }

