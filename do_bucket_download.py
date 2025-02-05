import os
import boto3
from utils.env_helper import env_get_contents

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

session = boto3.session.Session()
s3_client = session.client(
    's3',
    region_name=env_get_contents('REGION_NAME'),
    endpoint_url=env_get_contents('ENDPOINT_URL'),
    aws_access_key_id=env_get_contents('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=env_get_contents('AWS_SECRET_ACCESS_KEY')
)

def download_dir(prefix, bucket, local, client=s3_client):
    """
    params:
    - prefix: pattern to match in s3
    - local: local path to folder in which to place files
    - bucket: s3 bucket with target contents
    - client: initialized s3 client object
    """
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket':bucket,
        'Prefix':prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        print(f'|Baixando >>> {dest_pathname}')
        client.download_file(bucket, k, dest_pathname)

download_dir(
    prefix=env_get_contents('SOURCE_DIR'+'/'),
    bucket=env_get_contents('SOURCE_BUCKET'),
    local=os.path.join(BASE_DIR, 'downloads'),
)