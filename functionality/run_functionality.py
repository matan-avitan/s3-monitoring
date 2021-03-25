import time
import sched
from multiprocessing import Process
from functionality.uploadFileLatency import UploadFileLatency
from functionality.downloadFileLatency import DownloadFileLatency
from functionality.deleteFileLatency import DeleteFileLatency

loop = sched.scheduler(time.time, time.sleep)


def f1_run():
    s3_upload = UploadFileLatency()
    loop.enter(3, 1, f1, (loop, s3_upload))
    loop.run()


def f1(scheduler_loop, s3_upload):
    with s3_upload as s3:
        s3.run_functionality()
    loop.enter(3, 1, f1, (scheduler_loop, s3_upload))


def f2():
    s3_download = DownloadFileLatency()
    # with s3_download as s3:
    #     s3.run_functionality()


def f3():
    s3_delete = DeleteFileLatency()
    # with s3_delete as s3:
    #     s3.run_functionality()


if __name__ == "__main__":
    processes = [Process(target=f1_run), Process(target=f2), Process(target=f3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
