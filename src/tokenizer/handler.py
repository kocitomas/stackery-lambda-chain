from boto3 import client as boto3_client
import botocore.response as br
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
                                               InvocationType="RequestResponse",
                                               Payload=json.dumps(body))

    streaming_object = invoke_response["Payload"]
    res_json = json.loads(streaming_object.read().decode("utf-8"))

    response = {
        'statusCode': 200,
        'headers': { 'Content-Type': 'json'},
        'body': res_json
     }

    return response


