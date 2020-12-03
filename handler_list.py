import boto3
import os

dynamodb = boto3.resource('dynamodb')


def list_opinions(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()

    return result['Items']