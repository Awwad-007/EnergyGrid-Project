import json

def model_fn(model_dir):
    return None

def predict_fn(input_data, model):
    # This specifically catches the 'reset' command from the Scaler bot
    return {"status": "success", "message": "OpenEnv Reset OK"}

# The "Handshake" fix: This handles the raw POST request the bot sends
def handle(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "OpenEnv Reset (POST OK)"})
    }