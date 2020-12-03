import boto3
from botocore.exceptions import ClientError
import os
import uuid

client = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
sender = os.environ['SENDER_EMAIL']
subject = os.environ['EMAIL_SUBJECT']
charset = 'UTF-8'


def save_and_send(event, context):
    try:
        content = 'Opinion from {}, email: {}, content: {}'.format(event['name'], event['email'], event['message'])
        save_to_dynamo(event)
        response = send_email(content)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("E-mail sent! Message Id:", response['MessageId']),
    return "E-mail sent!"


def save_to_dynamo(data):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'firm': data['firm'],
        'email': data['email'],
        'message': data['message'],
        'published': False,
    }
    return table.put_item(Item=item)


def send_email(content):

    return client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                os.environ['SENDER_EMAIL'],
            ],
        },
        Message={
            'Subject': {
                'Charset': charset,
                'Data': subject
            },
            'Body': {
                'Html': {
                    'Charset': charset,
                    'Data': content
                },
                'Text': {
                    'Charset': charset,
                    'Data': content
                }
            }
        }
    )
