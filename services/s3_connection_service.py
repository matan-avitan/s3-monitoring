import boto3
import logging


class ServiceFormatter(logging.Formatter):
    def format(self, record):
        record.module = record.args.get('module')
        return super().format(record)


class S3ConnectionService(object):
    def __init__(self):
        self.access_key = "AKIAQSPNLRJYQFHUJLGS"
        self.secret = "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"
        self.bucket_name = "tech-interview-2513"
        self.name = "S3-Connection-Service"
        self.logger = logging.getLogger("S3")
        self.setup_logger()

    def setup_logger(self):
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            stream_handler = logging.StreamHandler()
            formatter = ServiceFormatter(f'%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    @property
    def connect(self):
        self.logger.info("Connect to S3", self.get_module())
        s3_connection = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret)
        return s3_connection

    def get_module(self):
        return {"module": self.name}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
