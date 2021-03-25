class S3ServiceConnection(object):
    def __init__(self):
        self.access_key = "AKIAQSPNLRJYQFHUJLGS"
        self.secret = "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"
        self.bucket_name = "tech-interview-2513"

    def connect(self):
        print(f"connect with {self.access_key} and {self.secret}")

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("disconnect")


