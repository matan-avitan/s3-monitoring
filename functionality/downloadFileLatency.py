from functionality.utils import latency_check

from services.s3_downloader_service import S3DownloaderService


class DownloadFileLatency(S3DownloaderService):

    def __init__(self):
        super(DownloadFileLatency, self).__init__()

    @latency_check
    def run_functionality(self):
        files = ['test_files/test.txt']
        self.download_files(files)
