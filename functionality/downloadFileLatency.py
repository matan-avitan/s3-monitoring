from datetime import datetime

from services.s3_downloader_service import S3DownloaderService


class DownloadFileLatency(S3DownloaderService):

    def __init__(self):
        super(DownloadFileLatency, self).__init__()

    def run_functionality(self):
        files = ['Ombudb(1).png']
        start_time = datetime.now()

        self.download_files(files)
        end_time = datetime.now()
        process_time = end_time - start_time
        print(f'the process (download) take - {process_time}')
