import hashlib
from functionality.utils import latency_check

from services.s3_downloader_service import S3DownloaderService
from services.s3_uploader_service import S3UploaderService


class HashFileTest(S3DownloaderService, S3UploaderService):

    def __init__(self):
        super(HashFileTest, self).__init__()
        self.name = 'S3-Hash-Test'

    @staticmethod
    def hash_file(file):
        hasher = hashlib.md5()
        with open(file, 'rb') as file_obj:
            data = file_obj.read()
            hasher.update(data)
        return hasher.hexdigest()

    @latency_check
    def run_functionality(self):
        self.logger.info("start hash test", self.get_extra_to_logger())
        file = 'test_files/hash_test/test.txt'
        start_hash_res = self.hash_file(file)
        self.upload_file(file)
        self.download_file(file)
        end_hash_res = self.hash_file(file)
        hash_status = 'Success' if start_hash_res == end_hash_res else 'Failed'
        self.logger.info(f"finsh hash test with status: {hash_status}", self.get_extra_to_logger())
        return self.test_id, self.name, hash_status
