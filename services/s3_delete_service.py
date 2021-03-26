from botocore.exceptions import ClientError
from services.s3_connection_service import S3ConnectionService


class S3DeleteService(S3ConnectionService):

    def __init__(self):
        super(S3DeleteService, self).__init__()
        self.name = "S3-Delete"

    def delete_file(self, file):
        self.logger.info(f"start to delete file: {file}", self.get_extra_to_logger())
        try:
            response = self.connect.delete_object(Bucket=self.bucket_name, Key=file)
            self.logger.info(f"finish to delete file: {file}", self.get_extra_to_logger())

        except (ClientError, ConnectionError) as e:
            self.logger.error(f"{e}", self.get_extra_to_logger())
            return False
        return True

