import requests
import time

def read_credentials(passfile):
    with open(passfile, 'r') as credits:
        decode_credits = credits.readlines()
    username = decode_credits[0].strip('\n')
    password = decode_credits[1].strip('\n')
    return username, password

def aoczone_login(username, password):
    url = 'http://aoczone.net/ucp.php?mode=login'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'username': username, 'password': password, 'login': 'Login'}
    login = requests.post(url, data=data, headers=headers)
    print(login.text)
    return login.cookies

def get_token(cookies):
    generator = cookies.itervalues()
    values = list(generator)
    token = values[2]
    return token

def post_record(record, subject, message, token, cookies):
    with open(record, 'rb') as infile:
        record_data = infile.read()

    current_time = int(time.time())
    url = 'http://aoczone.net/posting.php?mode=post&f=97'

    headers = {
        'Host': 'aoczone.net',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://aoczone.net/posting.php?mode=post&f=97',
        'Content-Type': 'multipart/form-data; boundary=---------------------------2445924741836591780646224716',
        'Content-Length': '2598',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    data = {
        'subject': subject,
        'addbbcode20': '100',
        'message': message,
        'comment_list[0]': '',
        'attachment_data[0][attach_id]': '151503',
        'attachment_data[0][is_orphan]': '1',
        'attachment_data[0][real_filename]': 'recording.zip',
        'attachment_data[0][attach_comment]': '',
        'post': 'Submit',
        'lastclick': current_time,
        'attach_sig': 'off',
        'creation_time': current_time,
        'form_token': '1738d139755591b18f0a4f1e569980280b6d0d64',
        'fileupload': record_data,
        'filecomment': '',
        'lobby_id': '132',
        'poll_title': '',
        'poll_option_text': '',
        'poll_max_options': '1',
        'poll_length': '0',
    }

    response = requests.post(url, headers=headers, cookies=cookies)
    print(response.text)


def rename_record():
    pass


username, password = read_credentials(passfile='.pass')
cookies = aoczone_login(username, password)
token = get_token(cookies)

post_record('recording.zip', 'testsub', 'testmessage', token, cookies)
