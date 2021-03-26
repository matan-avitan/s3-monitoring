import logging

from flask_restful import Resource


class LogsFormatter(logging.Formatter):
    def format(self, record):
        record.test_id = record.args.get('test_id')
        record.test_name = record.args.get('test_name')
        record.status = record.args.get('status')

        return super().format(record)


class BaseResource(Resource):
    LOG_FORMAT = '%(asctime)s - %(test_id)s - %(test_name)s - %(status)s - %(message)s'

    def __init__(self):
        self.logger = logging.getLogger("logger")
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler('logs.txt')
            formatter = LogsFormatter(self.LOG_FORMAT)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
