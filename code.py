import requests

def read_credentials(passfile):
    with open(passfile, 'r') as credits:
        decode_credits = credits.readlines()
    username = decode_credits[0].strip('\n')
    password = decode_credits[1].strip('\n')
    return username, password

def aoczone_login(username, password):
    url = 'http://aoczone.net/ucp.php?mode=login'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = 'username=' + username + '&password=' + password + '%40123&login=Login'
    login = requests.post(url, data=data, headers=headers)
    return login.cookies

def get_token(cookies):
    generator = cookies.itervalues()
    values = list(generator)
    token = values[2]
    return token

def post_record():
    pass

def rename_record():
    pass


username, password = read_credentials(passfile='.pass')
cookies = aoczone_login(username, password)
token = get_token(cookies)
