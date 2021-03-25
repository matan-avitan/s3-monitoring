from botocore.exceptions import ClientError
from services.s3_connection_service import S3ConnectionService


class S3DeleteService(S3ConnectionService):

    def __init__(self):
        super(S3DeleteService, self).__init__()

    def delete_file(self, file):
        print(f"delete {file}")
        try:
            response = self.connect.delete_object(Bucket=self.bucket_name, Key=file)
        except ClientError as e:
            return False
        return True

    def delete_files(self, files_to_delete):
        for file in files_to_delete:
            self.delete_file(file)
