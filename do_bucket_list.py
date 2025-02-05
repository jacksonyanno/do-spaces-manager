import os
import boto3
from utils.env_helper import env_get_contents

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=env_get_contents('REGION_NAME'),
    endpoint_url=env_get_contents('ENDPOINT_URL'),
    aws_access_key_id=env_get_contents('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=env_get_contents('AWS_SECRET_ACCESS_KEY')
)

print(client.list_buckets())

"""
**Request Syntax** 
::

    response = client.list_objects_v2(Bucket='h-agiliza-spaces',)
        Delimiter='string',
        EncodingType='url',
        MaxKeys=123,
        Prefix='string',
        ContinuationToken='string',
        FetchOwner=True|False,
        StartAfter='string',
        RequestPayer='requester',
        ExpectedBucketOwner='string'
    )
:type Bucket: string
:param Bucket: **[REQUIRED]** 

    Bucket name to list. 
"""