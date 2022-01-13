#coding = utf-8
'''
Created on Jan 8, 2022

@author: Dustin Lin
'''
import os
import datetime
import configparser
import requests

now = datetime.datetime.now()
config = configparser.ConfigParser()
str_config_path = os.path.join(os.getcwd(), "ini", "device_data.ini")
config.read(str_config_path)


def send_request(str_url, str_data):
    headers = eval(config_get("api_info", "request_header"))
    response = requests.put(str_url, json = {"edt": str_data}, headers = headers)
    res = response.json()
    print(res)
def log_title():
    date_time = now.strftime("%Y/%m/%d %H:%M:%S.%f")
    title = "Start from " + date_time
    print(title)
    
def result(int_data, int_start_data):
    today_total = str(int_data - int_start_data)
    today_final = str(int(today_total, 16))
    msg = str(datetime.datetime.now()) +  " today from :{} today total: {} to int: {}".format(int_start_data, (int_data - int_start_data), today_final) + "\n"
    #print(datetime.datetime.now(), "today from :{} today total: {} to int: {}".format(int_start_data, (int_data - int_start_data), today_final))

    return msg

def write_log_file(insert_data):
    file_title = now.strftime("%Y_%m_%d__%H_%M_%S_%f") + ".txt"
    path = os.path.join(os.getcwd(), "log", file_title)
    f = open(path, 'a')
    lines = insert_data
    f.writelines(lines)
    f.close()
    
def verify_init_value_isexist(task, scope):
    if config.has_section(task) is True:
        # section exist
        if config.has_option(task, scope) is True:
            # key exsit
            print("#Already has init value")
        else:
            # key not exist
            print("#Config add ->session: {} key: {}".format(task, scope))
            config_set(task, scope, "400")
    else:
        # section not exist
        print("#Create a new section")
        print("#Config add ->session: {} key: {}".format(task, scope))
        config_set_section(task)
        config_set(task, scope, "400")

def config_set_section(section):
    config.add_section(section)

def config_set(session, scope, value):
    config.set(session, scope, value)
    config.write(open(str_config_path, 'w'))

def config_get(session, scope):
    return config.get(session, scope)
    