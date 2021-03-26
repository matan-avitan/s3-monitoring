from botocore.exceptions import ClientError
from services.s3_connection_service import S3ConnectionService


class S3UploaderService(S3ConnectionService):

    def __init__(self):
        super(S3UploaderService, self).__init__()
        self.name = "S3-Uploader"

    def upload_file(self, file):
        self.logger.info(f"start to upload file: {file}", self.get_module())
        try:
            response = self.connect.upload_file(file, self.bucket_name, file)
            self.logger.info(f"finish to upload file: {file}", self.get_module())

        except ClientError as e:
            self.logger.error(f"{e}", self.get_module())
            return False
        return True

