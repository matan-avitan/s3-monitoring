import boto3


class S3ConnectionService(object):
    def __init__(self):
        self.access_key = "AKIAQSPNLRJYQFHUJLGS"
        self.secret = "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"
        self.bucket_name = "tech-interview-2513"

    @property
    def connect(self):
        s3_connection = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret)
        return s3_connection

    def __enter__(self):
        print("connecting")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("disconnect")
