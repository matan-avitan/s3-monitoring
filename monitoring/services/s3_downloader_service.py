from botocore.exceptions import ClientError
from services.s3_connection_service import S3ConnectionService


class S3DownloaderService(S3ConnectionService):

    def __init__(self):
        super(S3DownloaderService, self).__init__()
        self.name = "S3-Downloader"

    def download_file(self, file):
        self.logger.info(f"start to download file: {file}", self.get_extra_to_logger())
        try:
            with open(file, 'wb+') as f:
                self.logger.info("try to download", self.get_extra_to_logger())
                self.connect.download_fileobj(self.bucket_name, file, f)
            self.logger.info(f"finish to download file: {file}", self.get_extra_to_logger())
        except Exception as e:
            self.logger.error(f"{e}", self.get_extra_to_logger())

            return False
        return True
