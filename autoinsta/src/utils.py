import os
import json

def abs_path(local_path):
    return os.path.abspath(local_path)

def get_account_details():
    f = open('autoinsta/profiles/instagram.pass')
    details = f.readlines()
    return details[0], details[1]

def clean_log(message):
    print("*****", message, "*****")

def error_log(message):
    print("***** ERROR", message, "*****")

def get_json_value(j, key):
    valid = json.dumps(j)
    data = json.loads(valid)
    return data[key]