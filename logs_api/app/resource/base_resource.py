import logging

from flask_restful import Resource


class MyFormatter(logging.Formatter):
    def format(self, record):
        record.status = record.args.get('status')
        return super().format(record)


class BaseResource(Resource):

    def __init__(self):
        self.logger = logging.getLogger("logger")
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler('logs.txt')
            formatter = MyFormatter(f'%(asctime)s - %(levelname)s - Test status: %(status)s  - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
