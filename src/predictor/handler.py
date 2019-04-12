def handler(message, _context):
    print("Predictor is processing message: {}".format(message))

    return {"text": "No, you are the coolest!"}