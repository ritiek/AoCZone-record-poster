import requests

with open('.pass', 'r') as credits:
    decode_credits = credits.readlines()
    username = decode_credits[0].strip('\n')
    password = decode_credits[1].strip('\n')

url = 'http://aoczone.net/ucp.php?mode=login'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = 'username=' + username + '&password=' + password + '%40123&login=Login'

login = requests.post(url, data=data, headers=headers)
print(login.text)
