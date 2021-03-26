from flask_restful import reqparse
from logs_api.app.resource.base_resource import BaseResource

parser = reqparse.RequestParser()

parser.add_argument('test_id', type=str)
parser.add_argument('status', type=str)
parser.add_argument('msg', type=str)
parser.add_argument('test_name', type=str)


class Logs(BaseResource):

    def post(self):
        args = parser.parse_args()
        self.logger.info(args['msg'], {'status': args['status'],
                                       'test_id': args['test_id'],
                                       'test_name': args['test_name']})
        return {}
