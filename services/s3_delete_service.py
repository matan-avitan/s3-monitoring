from botocore.exceptions import ClientError
from services.s3_service_connection import S3ServiceConnection


class S3DeleteService(S3ServiceConnection):

    def __init__(self):
        super(S3DeleteService, self).__init__()

    def delete_file(self, file):
        print(f"delete {file}")
        try:
            response = self.connect.delete_object(self.bucket_name, file)
        except ClientError as e:
            return False
        return True

    def delete_files(self, files_to_delete):
        for file in files_to_delete:
            self.delete_file(file)
