from functionality.uploadFileLatency import UploadFileLatency

s3_upload = UploadFileLatency()

with s3_upload as s3:
    s3.run_functionality()
