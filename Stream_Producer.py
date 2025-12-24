import json
import random
import string
import boto3
from datetime import datetime

kinesis_client = boto3.client('kinesis')

STREAM_NAME = "my-kinesis-stream"   # 🔁 change this

def random_string(prefix, length=5):
    return prefix + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def lambda_handler(event, context):

    fake_data = {
        "event_id": random_string("evt-"),
        "user_id": random_string("user-"),
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "city": random.choice(["Pune", "Mumbai", "Nagpur", "Nashik"]),
        "timestamp": datetime.utcnow().isoformat()
    }

    response = kinesis_client.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(fake_data),
        PartitionKey=fake_data["user_id"]
    )

    return {
        "statusCode": 200,
        "message": "Record sent to Kinesis",
        "shard_id": response["ShardId"],
        "sequence_number": response["SequenceNumber"],
        "data": fake_data
    }