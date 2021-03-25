from services.s3_service_connection import S3ServiceConnection


class S3UploaderService(S3ServiceConnection):

    def __init__(self):
        super(S3UploaderService, self).__init__()

    @staticmethod
    def upload_file(file):
        print(f"upload {file}")

    def upload_files(self, files_to_upload):
        for file in files_to_upload:
            self.upload_file(file)
