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
    threads.append(threading.Thread(target = generator.pv_e0, args = (gene_job, device_type, device_id, e0_interval,)))
    threads.append(threading.Thread(target = generator.pv_e1, args = (gene_job, device_type, device_id, e1_interval,)))
    for i in range(0, 2):
        threads[i].start()

    
        
if __name__ == '__main__':
    argv = sys.argv[1:]
    device_id = argv[1]
    task = argv[0]
    if task == 'pv':
        scope = device_id + '_' + config_get("device_epc", "pv_cumulative")
        verify_init_value_isexist(task, scope)    
        pv(task, device_id)