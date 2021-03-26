import requests
from datetime import datetime


def latency_check(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        name, status, test_id = function(*args, **kwargs)
        end_time = datetime.now()
        process_time = end_time - start_time
        log = {
            'test_id': test_id,
            'test_name': name,
            'status': status,
            'msg': f'the process take - {process_time}'
        }

        result = requests.post('http://127.0.0.1:8080/api/log/', log)
        if result.status_code != 201:
            raise Exception(result.reason)

    return wrapper
