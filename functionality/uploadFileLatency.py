import os
from services.s3_uploader_service import S3UploaderService


class UploadFileLatency(S3UploaderService):

    def __init__(self):
        super(UploadFileLatency, self).__init__()

    def run_functionality(self):
        files = ['test_files/test.txt']
        self.upload_files(files)
