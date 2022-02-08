#coding = utf-8
'''
Created on Jan 8, 2022

@author: Dustin Lin
'''
import random
import time, datetime
from tool import result, write_log_file, config_set, config_get, send_request, verify_init_value_isexist
start_time = 12
end_time = 17
class generator():
    def __init__(self):
        pass
            
    def pv_instance(self, device_type, device_no, sleep_time):
        str_url = config_get("api_info", "pv_url").format(device_no, config_get("device_epc", "pv_instance"))
        while(True):
            int_now_hour = int(datetime.datetime.now().strftime('%H'))
            if int_now_hour >= start_time and int_now_hour < end_time:
                str_value = str(random.randrange(0, 1000))
            elif int_now_hour < start_time or int_now_hour >= end_time:
                str_value = str(0)
            str_data = str_value.zfill(4)
            send_request(str_url, str_data)
            print("Sleep for {} secs!!!".format(sleep_time))    
            time.sleep(int(sleep_time))
            
    def battery_instance(self, device_type, device_no, sleep_time):
        str_url = config_get("api_info", "battery_url").format(device_no, config_get("device_epc", "battery_elec_3"))
        while(True):
            str_value = str(random.randrange(10, 60))
            str_data = str_value
            send_request(str_url, str_data)
            print("Sleep for {} secs!!!".format(sleep_time))
            time.sleep(int(sleep_time))

    def fc_instance(self, device_type, device_no, sleep_time):
        str_url = config_get("api_info", "fc_url").format(device_no, config_get("device_epc", "fc_instance"))
        while(True):
            str_value = str(random.randrange(0, 1000))
            str_data = str_value.zfill(4)
            send_request(str_url, str_data)
            print("Sleep for {} secs!!!".format(sleep_time))
            time.sleep(int(sleep_time))    
    
    def accumulate(self, device_type, device_no, scope, sleep_time):
        epc = config_get("device_epc", scope)
        scope = device_no + "_" + config_get("device_epc", scope)
        verify_init_value_isexist(device_type, scope)
        config_value = device_type + "_url"
        str_url = config_get("api_info", config_value).format(device_no, epc)
        str_device_scope = device_no + "_" + epc
        int_start_data = int(config_get(device_type, str_device_scope))
        int_data = int_start_data
        while(True):
            int_now_hour = int(datetime.datetime.now().strftime('%H'))
            if int_now_hour >= start_time and int_now_hour < end_time:
                str_data = str(int_data)
                str_format_data = str_data.zfill(8)
                int_data = int_data + random.randrange(400, 2000, 400)
            elif int_now_hour < start_time or int_now_hour >= end_time:
                str_data = str(config_get(device_type, str_device_scope))
                str_format_data = str_data.zfill(8)
            send_request(str_url, str_format_data)
            msg = "Device: {} EPC: {} --> ".format(device_type, epc)
            msg = msg + result(int_data, int_start_data)
            write_log_file(msg)
            config_set(device_type, str_device_scope, str(int_data))         
            print("Sleep for {} secs!!!".format(sleep_time))
            time.sleep(int(sleep_time))
        
    
        
if __name__ == '__main__':
    #job = generator()
    #job.pv_e0(2, 1)
    pass
