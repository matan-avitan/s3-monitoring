from functionality.uploadFileLatency import UploadFileLatency
from functionality.downloadFileLatency import DownloadFileLatency

s3_upload = UploadFileLatency()

with s3_upload as s3:
    s3.run_functionality()

s3_download = DownloadFileLatency()
with s3_download as s3:
    s3.run_functionality()
