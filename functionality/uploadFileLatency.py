from datetime import datetime

from services.s3_uploader_service import S3UploaderService


class UploadFileLatency(S3UploaderService):

    def __init__(self):
        super(UploadFileLatency, self).__init__()

    def run_functionality(self):
        files = ['test_files/test.txt']
        start_time = datetime.now()

        self.upload_files(files)
        end_time = datetime.now()
        process_time = end_time - start_time
        print(f'the process (upload) take - {process_time}')
