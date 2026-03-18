import boto3

def get_bedrock_client():
    return boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
    )


def get_s3_client():
    return boto3.client("s3")