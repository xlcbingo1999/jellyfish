
import time
import os

print("begin sleep")
# time.sleep(5)
print("suee")


def set_process_nice(nice_value=0):
    my_pid = os.getpid()
    os.system(f"sudo renice -n {nice_value} -p {my_pid}") # TODO(xlc): 设置优先级失败?
    print("success ")
    
# server: 10.43.229.120
# client: 10.43.229.56
# manager: 10.43.229.166

server_ip=10.43.229.120 \
server_username=ubuntu \
client_ip=10.43.229.56 \
client_username=ubuntu \
total_iter=1 \
network_trace_type=synthetic_trace \
./run_experiments.sh > /home/ubuntu/jellyfish/temp_result.log


# base_root_path=/home/ubuntu/jellyfish \
# src_manager_path=src/experiment_manager \
# bash ${base_root_path}/${src_manager_path}/run_experiments.sh \
# > ${base_root_path}/logs/experiment_manager/${network_trace_type}/

pkill run.sh; pkill python3; sudo pkill shape_tbf
ps -ef | grep "/bin/bash /home/ubuntu/jellyfish/src/client/run_network_shaping.sh" | grep -v grep | awk '{print $2}' | xargs -r kill


# ps -ef | grep "/bin/bash /home/ubuntu/jellyfish/src/client/run.sh" | grep -v grep | awk '{print $2}' | xargs -r kill
# ps -ef | grep "python3 /home/ubuntu/jellyfish/src/client/main.py" | grep -v grep | awk '{print $2}' | xargs -r kill

