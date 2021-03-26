from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('insertion_time', type=str)
parser.add_argument('status', type=str)
parser.add_argument('msg', type=str)


class Logs(Resource):

    def post(self):
        args = parser.parse_args()
        log_msg = f"{args['insertion_time']} - {args['status']} - {args['msg']}"
        print(log_msg)
        return {}
