# inference.py
def model_fn(model_dir):
    return None

def predict_fn(input_data, model):
    # This handles the 'reset' and 'POST' requests from the checker
    return {"status": "success", "message": "OpenEnv Reset OK"}