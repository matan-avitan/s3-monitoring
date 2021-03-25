from functionality.uploadFileLatency import UploadFileLatency

s3_upload = UploadFileLatency()
with s3_upload:
    s3_upload.run_functionality()
