import uuid
import requests
from datetime import datetime


def latency_check(function):
    def wrapper(*args, **kwargs):
        test_id = str(uuid.uuid4())
        start_time = datetime.now()
        name, status = function(*args, **kwargs)
        end_time = datetime.now()
        process_time = end_time - start_time
        log = {
            'test_id': test_id,
            'test_name': name,
            'status': status,
            'msg': f'the process take - {process_time}'
        }

        requests.post('http://127.0.0.1:8080/api/log/', log)

    return wrapper
