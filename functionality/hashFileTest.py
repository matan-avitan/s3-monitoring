import hashlib
from functionality.utils import latency_check

from services.s3_downloader_service import S3DownloaderService
from services.s3_uploader_service import S3UploaderService


class HashFileTest(S3DownloaderService, S3UploaderService):

    def __init__(self):
        super(HashFileTest, self).__init__()
        self.name = 'S3-Hash-Test'

    @latency_check
    def run_functionality(self):
        self.logger.info("start test", self.get_extra_to_logger())
        file = 'test_files/hash_test/test.txt'

        download_status = 'Success' if self.download_file(file) else 'Failed'
        return self.test_id, self.name, download_status
