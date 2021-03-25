import boto3
import logging


class S3ConnectionService(object):
    def __init__(self):
        self.access_key = "AKIAQSPNLRJYQFHUJLGS"
        self.secret = "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"
        self.bucket_name = "tech-interview-2513"
        self.name = "S3-Connection-Service"
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("S3")

    @property
    def connect(self):
        s3_connection = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret)
        return s3_connection

    def __enter__(self):
        self.logger.info("Connect to s3")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.info("Disconnect from s3")
