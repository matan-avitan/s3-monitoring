import time
import sched
from run.conf import Conf
from multiprocessing import Process
from functionality.uploadFileLatencyTest import UploadFileLatency
from functionality.downloadFileLatencyTest import DownloadFileLatency
from functionality.deleteFileLatencyTest import DeleteFileLatency
from functionality.hashFileTest import HashFileTest

loop = sched.scheduler(time.time, time.sleep)
loop2 = sched.scheduler(time.time, time.sleep)
loop3 = sched.scheduler(time.time, time.sleep)
loop4 = sched.scheduler(time.time, time.sleep)


def upload_file_latency_loop():
    loop.enter(Conf.UPLOADER_TIME_INTERVAL, 1, upload_file_latency, (loop,))
    loop.run()


def upload_file_latency(scheduler_loop):
    s3_upload = UploadFileLatency()
    with s3_upload as s3:
        s3.run_functionality()
    loop.enter(Conf.UPLOADER_TIME_INTERVAL, 1, upload_file_latency, (scheduler_loop,))


def download_file_latency_loop():
    loop.enter(Conf.DOWNLOADER_TIME_INTERVAL, 1, download_file_latency, (loop2,))
    loop.run()


def download_file_latency(scheduler_loop):
    s3_download = DownloadFileLatency()

    with s3_download as s3:
        s3.run_functionality()
    loop.enter(Conf.DOWNLOADER_TIME_INTERVAL, 1, download_file_latency, (scheduler_loop,))


def delete_file_latency_loop():
    loop.enter(Conf.DELETE_TIME_INTERVAL, 1, delete_file_latency, (loop3,))
    loop.run()


def delete_file_latency(scheduler_loop):
    s3_delete = DeleteFileLatency()

    with s3_delete as s3:
        s3.run_functionality()
    loop.enter(Conf.DELETE_TIME_INTERVAL, 1, delete_file_latency, (scheduler_loop,))


def hash_file_loop():
    loop.enter(Conf.HASH_TIME_INTERVAL, 1, hash_file, (loop3,))
    loop.run()


def hash_file(scheduler_loop):
    s3_hash = HashFileTest()

    with s3_hash as s3:
        s3.run_functionality()
    loop.enter(Conf.HASH_TIME_INTERVAL, 1, hash_file, (scheduler_loop,))


if __name__ == "__main__":
    processes = [Process(target=upload_file_latency_loop), Process(target=download_file_latency_loop),
                 Process(target=delete_file_latency_loop), Process(target=hash_file_loop)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
