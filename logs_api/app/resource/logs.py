import logging

from flask_restful import reqparse
from logs_api.app.resource.base_resource import BaseResource

parser = reqparse.RequestParser()
parser.add_argument('insertion_time', type=str)
parser.add_argument('status', type=str)
parser.add_argument('msg', type=str)


class Logs(BaseResource):

    def post(self):
        args = parser.parse_args()
        log_msg = f"{args['insertion_time']} - {args['status']} - {args['msg']}"
        self.logger.info(log_msg, {'status': args['status']})
        # print(log_msg)
        return {}
