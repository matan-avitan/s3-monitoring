import boto3
import uuid
import logging
from services.services_utils import try_get_env
from services.services_conf import ServicesConf


class ServiceFormatter(logging.Formatter):
    def format(self, record):
        record.module = record.args.get('module')
        record.test_id = record.args.get('test_id')
        return super().format(record)


class S3ConnectionService(object):
    def __init__(self):
        self.access_key = try_get_env("ACCESS_KEY", ServicesConf.ACCESS_KEY)
        self.secret = try_get_env("SECRET", ServicesConf.SECRET)
        self.bucket_name = ServicesConf.BUCKET_NAME
        self.name = "S3-Connection-Service"
        self.logger = logging.getLogger("S3")
        self.test_id = str(uuid.uuid4())
        self.setup_logger()

    def setup_logger(self):
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            stream_handler = logging.StreamHandler()
            formatter = ServiceFormatter(ServicesConf.FORMATTER)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    @property
    def connect(self):
        self.logger.info("Connect to S3", self.get_extra_to_logger())
        try:
            s3_connection = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret)
            return s3_connection
        except Exception as e:
            self.logger.error(f"Can't connect to S3 server - error:{str(e)}", self.get_extra_to_logger())
            raise ConnectionError

    def get_extra_to_logger(self):
        return {"module": self.name, "test_id": self.test_id}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
