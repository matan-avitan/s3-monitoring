from services.s3_service_connection import S3ServiceConnection


class S3DownloaderService(S3ServiceConnection):

    def __init__(self):
        super(S3DownloaderService, self).__init__()

    @staticmethod
    def download_file(file):
        print(f"download {file}")

    def download_files(self, files_to_upload):
        for file in files_to_upload:
            self.download_file(file)
