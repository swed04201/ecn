#coding = utf-8
'''
Created on Jan 8, 2022

@author: Dustin Lin
'''
import random
import time
from tool import result, write_log_file, config_set, config_get, send_request

class generator():
    def __init__(self):
        pass
            
    def pv_e0(self, device_type, device_no, sleep_time):
        str_url = config_get("api_info", "pv_url").format(device_no, config_get("device_epc", "pv_instance"))
        while(True):
            str_value = str(random.randrange(0, 1000))
            str_data = str_value.zfill(4)
            send_request(str_url, str_data)
            print("Sleep for {} secs!!!".format(sleep_time))
            time.sleep(int(sleep_time))
    
    def pv_e1(self, device_type, device_no, sleep_time):
        str_url = config_get("api_info", "pv_url").format(device_no, config_get("device_epc", "pv_cumulative"))
        str_device_scope = device_no + '_' + config_get("device_epc", "pv_cumulative")
        int_start_data = int(config_get(device_type, str_device_scope))
        int_data = int_start_data
        while(True):
            str_data = str(int_data)
            str_fix_data = str_data.zfill(8)
            int_data = int_data + random.randrange(400, 2000, 400)
            send_request(str_url, str_fix_data)
            msg = result(int_data, int_start_data)
            write_log_file(msg)
            config_set(device_type, str_device_scope, str(int_data))         
            print("Sleep for {} secs!!!".format(sleep_time))
            time.sleep(int(sleep_time))


       
        
if __name__ == '__main__':
    job = generator()
    job.pv_e0(2, 1)
