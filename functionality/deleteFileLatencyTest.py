from functionality.utils import latency_check
from services.s3_delete_service import S3DeleteService
from functionality.functionality_conf import FunctionalityConf


class DeleteFileLatency(S3DeleteService):

    def __init__(self):
        super(DeleteFileLatency, self).__init__()
        self.name = 'S3-Delete-Latency'

    @latency_check
    def run_functionality(self):
        self.logger.info("start deleting", self.get_extra_to_logger())
        delete_status = 'Success' if self.delete_file(FunctionalityConf.UPLOAD_FILE) else 'Failed'
        return self.test_id, self.name, delete_status
