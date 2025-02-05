import os
import boto3
from utils.content import CONTENT_TYPE_DICT
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

def upload_dir(source_dir,  bucket, target_dir='', client=s3_client):

    paths = [source_dir]
    for path in paths:
        dirs = os.listdir(path)
        for dir in dirs:
            curr_pathname = os.path.join(path, dir)
            if os.path.isdir(curr_pathname): #checks if path is a directory
                paths.append(curr_pathname)
            else: #is file
                file_name, file_extension = os.path.splitext(curr_pathname)                
                key =  target_dir + curr_pathname.replace(source_dir, '')    
                extra_args={
                    'ACL': 'public-read',
                    'ContentType': CONTENT_TYPE_DICT.get(file_extension.lower(), None)
                }
                print(f'|Subindo >>> {curr_pathname}')
                client.upload_file(curr_pathname, bucket, key, ExtraArgs=extra_args)
                file_url = '%s/%s/%s' % (client.meta.endpoint_url, bucket, key)
                print("**** esta é a url :: " + file_url)

upload_dir(
    source_dir=os.path.join(BASE_DIR, 'downloads/' + env_get_contents('SOURCE_LOCAL_DIR')),
    bucket=env_get_contents('TARGET_BUCKET'),
    target_dir=env_get_contents('TARGET_DIR')
)

"""
upload_file(Filename, Bucket, Key, ExtraArgs=None, Callback=None, Config=None)
Upload a file to an S3 object.

Usage:

    import boto3
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
    Similar behavior as S3Transfer's upload_file() method, except that parameters are capitalized. Detailed examples can be found at S3Transfer's Usage.

Parameters
    Filename (str) -- The path to the file to upload.
    Bucket (str) -- The name of the bucket to upload to.
    Key (str) -- The name of the key to upload to.
    ExtraArgs (dict) -- Extra arguments that may be passed to the client operation. For allowed upload arguments see boto3.s3.transfer.S3Transfer.ALLOWED_UPLOAD_ARGS.
    Callback (function) -- A method which takes a number of bytes transferred to be periodically called during the upload.
    Config (boto3.s3.transfer.TransferConfig) -- The transfer configuration to be used when performing the transfer.
"""