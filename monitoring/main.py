from functionality import *
from conf import Conf
from multiprocessing import Process
from processes.proccess_loop import ProcessLoop


def process_test(obj, interval):
    p = ProcessLoop(interval, Conf.PRIORITY)
    p.create_loop(obj)


if __name__ == "__main__":
    """
    Create 4 process for monitoring s3
    """
    processes = [Process(target=process_test, args=(UploadFileLatency, Conf.UPLOADER_TIME_INTERVAL)),
                 Process(target=process_test, args=(DownloadFileLatency, Conf.DOWNLOADER_TIME_INTERVAL)),
                 Process(target=process_test, args=(DeleteFileLatency, Conf.DELETE_TIME_INTERVAL)),
                 Process(target=process_test, args=(HashFileTest, Conf.HASH_TIME_INTERVAL))]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
