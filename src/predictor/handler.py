def handler(message, context):
    body = message["body"]

    print("Predictor is processing message: {}".format(body))

    return {"text": "No, you are the coolest!"}