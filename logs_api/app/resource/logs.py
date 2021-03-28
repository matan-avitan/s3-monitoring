from flask import Response
from http import HTTPStatus
from app.resource.resource_utils import error_handler
from flask_restful import reqparse
from app.resource.base_resource import BaseResource

parser = reqparse.RequestParser()

parser.add_argument('test_id', type=str)
parser.add_argument('status', type=str)
parser.add_argument('msg', type=str)
parser.add_argument('test_name', type=str)


class Logs(BaseResource):

    @error_handler
    def post(self):
        args = parser.parse_args()
        self.logger.info(args['msg'], {'status': args['status'],
                                       'test_id': args['test_id'],
                                       'test_name': args['test_name']})
        return Response({"result": "success enter new log"}, status=HTTPStatus.CREATED)
