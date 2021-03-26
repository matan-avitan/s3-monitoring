from functionality.utils import latency_check

from services.s3_delete_service import S3DeleteService


class DeleteFileLatency(S3DeleteService):

    def __init__(self):
        super(DeleteFileLatency, self).__init__()
        self.name = 'S3-Delete-Latency'

    @latency_check
    def run_functionality(self):
        self.logger.info("start deleting", {'module': self.name})
        files = 'test_files/test.txt'
        delete_status = 'Success' if self.delete_file(files) else 'Failed'
        return self.name, delete_status
