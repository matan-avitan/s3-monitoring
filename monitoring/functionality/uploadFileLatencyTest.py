from functionality.utils import latency_check
from services.s3_uploader_service import S3UploaderService
from functionality.functionality_conf import FunctionalityConf


class UploadFileLatency(S3UploaderService):
    """
    try to upload a file with upload service.
    return the status.
    it cover with latency check decorator that send to logs_api the result with how log it takes
    """

    def __init__(self):
        super(UploadFileLatency, self).__init__()
        self.name = 'S3-Upload-Latency'

    @latency_check
    def run_functionality(self):
        self.logger.info("start uploading test", self.get_extra_to_logger())
        upload_status = 'Success' if self.upload_file(FunctionalityConf.UPLOAD_FILE) else 'Failed'
        return self.test_id, self.name, upload_status
