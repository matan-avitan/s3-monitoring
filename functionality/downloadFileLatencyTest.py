from functionality.utils import latency_check

from services.s3_downloader_service import S3DownloaderService


class DownloadFileLatency(S3DownloaderService):

    def __init__(self):
        super(DownloadFileLatency, self).__init__()
        self.name = 'S3-Download-Latency'

    @latency_check
    def run_functionality(self):
        self.logger.info("start download", self.get_extra_to_logger())
        file = 'test_files/downloader_test/test.txt'
        download_status = 'Success' if self.download_file(file) else 'Failed'
        return self.test_id, self.name, download_status
