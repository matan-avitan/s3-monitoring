from datetime import datetime


def latency_check(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        function(*args, **kwargs)
        end_time = datetime.now()
        process_time = end_time - start_time
        print(f'the process (download) take - {process_time}')

    return wrapper
