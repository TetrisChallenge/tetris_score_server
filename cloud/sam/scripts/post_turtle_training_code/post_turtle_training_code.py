import boto3
import os
import subprocess
import json
import glob

FRONTEND_ORIGIN = os.environ["FRONTEND_ORIGIN"]
LAMBDA_TASK_ROOT = os.environ["LAMBDA_TASK_ROOT"]
SUBPROCESS_TIMEOUT_LIMIT = 3


def lambda_handler(event: dict, context):
    section = event['pathParameters']['section']
    response = evaluation(event, context)
    
    for p in glob.glob("/tmp/*"):
       if os.path.isfile(p):
           os.remove(p)
           
    return response


def evaluation(event: dict, context):
    section = event['pathParameters']['section']
    id = event['pathParameters']['id']

    python_file_path = "/tmp/main.py"
    with open(python_file_path , mode='w') as f:
        f.write(event["body"])
    
    try:
        proc = subprocess.run(["xvfb-run", "-a", "python", python_file_path], capture_output=True, timeout=SUBPROCESS_TIMEOUT_LIMIT, check=True)
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
            },
            "isBase64Encoded": True,
            "body": open('/tmp/canvas.svg', 'rb').read().encode('base64')
        }
    except subprocess.TimeoutExpired:
        response = {
            "statusCode": 400,
            "body": "Time expired error",
            "headers": {
                "Content-Type": "text/plain",
            },
        }
    except subprocess.CalledProcessError:
        response = {
            "statusCode": 400,
            "body": "Runtime error",
            "headers": {
                "Content-Type": "text/plain",
            },
        }

    for f in os.listdir("/tmp"):
        os.remove(os.path.join(dir, f))

    return response
