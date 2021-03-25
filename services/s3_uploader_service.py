from botocore.exceptions import ClientError
from services.s3_connection_service import S3ConnectionService


class S3UploaderService(S3ConnectionService):

    def __init__(self):
        super(S3UploaderService, self).__init__()

    def upload_file(self, file):
        print(f"upload {file}")
        try:
            response = self.connect.upload_file(file, self.bucket_name, file)
        except ClientError as e:
            return False
        return True

    def upload_files(self, files_to_upload):
        for file in files_to_upload:
            self.upload_file(file)
