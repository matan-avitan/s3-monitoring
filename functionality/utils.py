import requests
from datetime import datetime


def latency_check(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function(*args, **kwargs)
        end_time = datetime.now()
        process_time = end_time - start_time
        log = {
            'insertion_time': datetime.now(),
            'status': 'success',
            'msg': f'the process (download) take - {process_time}'
        }

        requests.post('http://127.0.0.1:8080/api/log/', log)

    return wrapper
