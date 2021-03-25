from services.s3_delete_service import S3DeleteService
from datetime import datetime


class DeleteFileLatency(S3DeleteService):

    def __init__(self):
        super(DeleteFileLatency, self).__init__()

    def run_functionality(self):
        files = ['test_files/test.txt']
        start_time = datetime.now()
        self.delete_files(files)
        end_time = datetime.now()
        process_time = end_time - start_time
        print(f'the process (delete) take - {process_time}')
