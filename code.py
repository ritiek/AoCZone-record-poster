import requests

username = 'username'
password = 'password'

url = 'http://aoczone.net/ucp.php?mode=login'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = 'username=' + username + '&password=' + password + '%40123&login=Login'

login = requests.post(url, data=data, headers=headers)
