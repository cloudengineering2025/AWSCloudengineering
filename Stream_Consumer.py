import json
import base64

def lambda_handler(event, context):

    for record in event['Records']:
        payload = base64.b64decode(
            record['kinesis']['data']
        ).decode('utf-8')

        data = json.loads(payload)

        print("Received Record:")
        print(json.dumps(data, indent=2))

        # 👉 Example processing
        if data["temperature"] > 35:
            print("🔥 High temperature alert!")

    return {
        "statusCode": 200,
        "message": "Records processed successfully"
    }