from boto3 import client as boto3_client
import json
import os

# start lambda client
lambda_client = boto3_client("lambda")

# load env vars
REMOTE_LAMBDA_NAME = os.environ["FUNCTION_NAME"]

def handler(message, context):
    body = message["body"]

    print("tokenizer forwarding inbound message to predictor: {}".format(body))

    invoke_response = lambda_client.invoke(FunctionName=REMOTE_LAMBDA_NAME,
                                               InvocationType="Event",
                                               Payload=json.dumps(body))

    print(invoke_response)
    # response = {
    #     'statusCode': 200,
    #     'headers': { 'Content-Type': 'json' },
    #     'body': invoke_response
    #  }
    #
    # return response

    return {"body": "you are the coolest"}

