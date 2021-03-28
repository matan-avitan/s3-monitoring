import sched
import time

loop = sched.scheduler(time.time, time.sleep)


class ProcessLoop(object):

    def __init__(self, interval, priority):
        self.interval = interval
        self.priority = priority

    def create_loop(self, obj):
        loop.enter(self.interval, self.priority, ProcessLoop.process_loop, (self, loop, obj))
        loop.run()

    def process_loop(self, scheduler_loop, obj):
        try:
            s3_obj = obj()
            with s3_obj as s3:
                s3.run_functionality()
        except Exception as e:
            print(str(e))
        finally:
            loop.enter(self.interval, self.priority, ProcessLoop.process_loop, (self, scheduler_loop, obj))
