
import time
import os

print("begin sleep")
# time.sleep(5)
print("suee")


def set_process_nice(nice_value=0):
    my_pid = os.getpid()
    os.system(f"sudo renice -n {nice_value} -p {my_pid}") # TODO(xlc): 设置优先级失败?
    print("success ")