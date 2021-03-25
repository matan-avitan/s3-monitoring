from botocore.exceptions import ClientError

from services.s3_connection_service import S3ConnectionService


class S3DownloaderService(S3ConnectionService):

    def __init__(self):
        super(S3DownloaderService, self).__init__()
        self.name = "S3-Downloader"

    def download_file(self, file):
        self.logger.info(f"download file: {file}", self.get_module())
        try:
            with open(file, 'wb+') as f:
                self.connect.download_fileobj(self.bucket_name, file, f)
        except ClientError as e:
            self.logger.error(f"{e}", self.get_module())

            return False
        return True

    def download_files(self, files_to_download):
        for file in files_to_download:
            self.download_file(file)
