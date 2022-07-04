def get_account_details():
    f = open('profiles/instagram.pass')
    details = f.readlines()
    return details[0], details[1]