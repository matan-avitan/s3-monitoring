from services.s3_connection_service import S3ConnectionService


class S3DeleteService(S3ConnectionService):
    """
    Delete service - connect to s3 and delete specific file it get
    """

    def __init__(self):
        super(S3DeleteService, self).__init__()
        self.name = "S3-Delete"

    def delete_file(self, file):
        self.logger.info(f"start to delete file: {file}", self.get_extra_to_logger())
        try:
            self.logger.info("try to delete", self.get_extra_to_logger())
            self.connect.delete_object(Bucket=self.bucket_name, Key=file)
            self.logger.info(f"finish to delete file: {file}", self.get_extra_to_logger())
        except Exception as e:
            self.logger.error(f"{e}", self.get_extra_to_logger())
            return False
        return True
