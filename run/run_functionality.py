import time
import sched
from multiprocessing import Process
from functionality.uploadFileLatency import UploadFileLatency
from functionality.downloadFileLatency import DownloadFileLatency
from functionality.deleteFileLatency import DeleteFileLatency

loop = sched.scheduler(time.time, time.sleep)
loop2 = sched.scheduler(time.time, time.sleep)
loop3 = sched.scheduler(time.time, time.sleep)

TIME_INTERVAL = 1


def upload_file_latency_loop():
    s3_upload = UploadFileLatency()
    loop.enter(TIME_INTERVAL, 1, upload_file_latency, (loop, s3_upload))
    loop.run()


def upload_file_latency(scheduler_loop, s3_upload):
    with s3_upload as s3:
        s3.run_functionality()
    loop.enter(TIME_INTERVAL, 1, upload_file_latency, (scheduler_loop, s3_upload))


def download_file_latency_loop():
    s3_download = DownloadFileLatency()
    loop.enter(TIME_INTERVAL, 1, download_file_latency, (loop2, s3_download))
    loop.run()


def download_file_latency(scheduler_loop, s3_download):
    with s3_download as s3:
        s3.run_functionality()
    loop.enter(TIME_INTERVAL, 1, download_file_latency, (scheduler_loop, s3_download))


def delete_file_latency_loop():
    s3_delete = DeleteFileLatency()
    loop.enter(TIME_INTERVAL, 1, delete_file_latency, (loop3, s3_delete))
    loop.run()


def delete_file_latency(scheduler_loop, s3_delete):
    with s3_delete as s3:
        s3.run_functionality()
    loop.enter(TIME_INTERVAL, 1, delete_file_latency, (scheduler_loop, s3_delete))


if __name__ == "__main__":
    processes = [Process(target=upload_file_latency_loop), Process(target=download_file_latency_loop),
                 Process(target=delete_file_latency_loop)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
