from functionality.utils import latency_check

from services.s3_delete_service import S3DeleteService


class DeleteFileLatency(S3DeleteService):

    def __init__(self):
        super(DeleteFileLatency, self).__init__()

    @latency_check
    def run_functionality(self):
        files = ['test_files/test.txt']
        self.delete_files(files)
