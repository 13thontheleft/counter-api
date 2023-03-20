import boto3
from botocore.exceptions import ClientError
import json


class CVCounter:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('cv-counter')

    def table_exists(self):
        try:
            self.table.load()
            exists = True

        except ClientError as err:
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                exists = False
            else:
                print(
                    f"Couldn't check if table exists. Here's why: "
                    f"{err.response['Error']['Code']}: {err.response['Error']['Message']}")
                raise
        return exists

    def increment_total(self):
        item = self.get_total()
        total = item['total']
        total += 1
        self.table.put_item(Item={
            'site_id': 'cv',
            "total": total
        })

    def get_total(self):
        try:
            response = self.table.get_item(Key={'site_id': 'cv'})
            return response['Item']
        except KeyError:
            item = {'site_id': 'cv', 'total': 0}
            self.table.put_item(Item=item)
            return item


def lambda_handler(event, context):
    cv_counter = CVCounter()
    if cv_counter.table_exists():
        cv_counter.increment_total()
        item = cv_counter.get_total()
        total = item['total']
        json_string = f'"total": {total}'
        return json.dumps({
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": f'{json_string}',
        })
    else:
        raise

