import requests
from datetime import datetime


def latency_check(function):
    """
    The function cover all monitors.
    it put start time var, run the monitor and then put end time var.
    calculate the diff and then send to api_logs the data from monitoring.
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        name, status, test_id = function(*args, **kwargs)
        end_time = datetime.now()
        process_time = end_time - start_time
        log = {
            'test_id': test_id,
            'test_name': name,
            'status': status,
            'msg': f'the process take: {process_time}'
        }

        result = requests.post('http://127.0.0.1/api/log/', log)
        if result.status_code != 201:
            raise Exception(result.reason)

    return wrapper
