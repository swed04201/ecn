#coding = utf-8
'''
Created on Jan 8, 2022

@author: Dustin Lin
'''
import threading, sys
from tool import config_get, verify_init_value_isexist
from generator import generator

def pv(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    e0_interval = config_get("device_scope_interval", "pv_e0")
    e1_interval = config_get("device_scope_interval", "pv_e1")
    threads.append(threading.Thread(target = generator.pv_instance, args = (gene_job, device_type, device_id, e0_interval,)))
    threads.append(threading.Thread(target = generator.pv_accumulate, args = (gene_job, device_type, device_id, e1_interval,)))
    for i in range(0, 2):
        threads[i].start()

def battery(device_type, device_id):
    gene_job = generator()
    running = threading.Event()
    running.set()
    threads = []
    a4_interval = config_get("device_scope_interval", "battery_a4")
    a5_interval = config_get("device_scope_interval", "battery_a5") 
    a8_interval = config_get("device_scope_interval", "battery_a8")
    a9_interval = config_get("device_scope_interval", "battery_a9") 
    d6_interval = config_get("device_scope_interval", "battery_d6") 
    d8_interval = config_get("device_scope_interval", "battery_d8") 
    e2_interval = config_get("device_scope_interval", "battery_e2") 
    e4_interval = config_get("device_scope_interval", "battery_e4")
    threads.append(threading.Thread(target = generator.battery_instance, args = (gene_job, device_type, device_id, e4_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_char_elec_eneg", a4_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_dischar_elec_eneg", a5_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_ac_cumu_char_elec_eneg", a8_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_ac_cumu_dischar_elec_eneg", a9_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_cumu_char_elec_eneg", d6_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_cumu_dischar_elec_eneg", d8_interval)))
    threads.append(threading.Thread(target = generator.battery_accumulate, args = (gene_job, device_type, device_id, "battery_elec_1", e2_interval)))
    for i in range(0, 8):
        threads[i].start()
    
    
    
    
        
if __name__ == '__main__':
    argv = sys.argv[1:]
    device_id = argv[1]
    task = argv[0]
    if task == 'pv':  
        pv(task, device_id)
    elif task == 'battery':  
        battery(task, device_id)