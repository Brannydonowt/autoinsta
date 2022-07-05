def get_account_details():
    f = open('autoinsta/profiles/instagram.pass')
    details = f.readlines()
    return details[0], details[1]

def clean_log(message):
    print("*****", message, "*****")

def error_log(message):
    print("***** ERROR", message, "*****")