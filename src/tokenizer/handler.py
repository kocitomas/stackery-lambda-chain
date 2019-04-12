from boto3 import client as boto3_client
import json
import os

# start lambda client
lambda_client = boto3_client("lambda")

# load env vars
REMOTE_LAMBDA_NAME = os.environ["FUNCTION_NAME"]

def handler(message, _context):
    body = message["body"]

    print("tokenizer forwarding inbound message to predictor: {}".format(body))

    invoke_response = lambda_client.invoke(FunctionName=REMOTE_LAMBDA_NAME,
                                               InvocationType="RequestResponse",
                                               Payload=json.dumps(body))

    print("tokenizer received responses from predictor: {}".format(invoke_response))

    streaming_object = invoke_response["Payload"]

    body = streaming_object.read().decode('utf-8')

    response = {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json'},
        'body': body
     }

    return response


