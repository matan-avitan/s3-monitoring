from functionality.utils import latency_check
from services.s3_uploader_service import S3UploaderService


class UploadFileLatency(S3UploaderService):

    def __init__(self):
        super(UploadFileLatency, self).__init__()
        self.name = 'S3-Upload-Latency'

    @latency_check
    def run_functionality(self):
        self.logger.info("start uploading", {'module': self.name})
        files = 'test_files/test.txt'
        upload_status = 'Success' if self.upload_file(files) else 'Failed'
        return self.name, upload_status
