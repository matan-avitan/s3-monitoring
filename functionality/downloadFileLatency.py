import os
from services.s3_downloader_service import S3DownloaderService


class DownloadFileLatency(S3DownloaderService):

    def __init__(self):
        super(DownloadFileLatency, self).__init__()

    def run_functionality(self):
        files = ['Ombudb(1).png']
        self.download_files(files)
