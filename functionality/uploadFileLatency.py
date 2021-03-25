from services.s3_uploader_service import S3UploaderService


class UploadFileLatency(S3UploaderService):

    def __init__(self):
        super(UploadFileLatency, self).__init__()

    def run_functionality(self):
        files = ['asdasd.t', 'asdasd.t', 'qaweqw.b']
        self.upload_files(files)


s3_upload = UploadFileLatency()
with s3_upload:
    s3_upload.run_functionality()
