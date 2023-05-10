import os
import ssl
import adafruit_requests


def pushToLine(cnPool,message):
    requests = adafruit_requests.Session(cnPool,ssl.create_default_context())
    url = f'https://notify-api.line.me/api/notify'
    token = os.getenv('LINE_TOKEN')
    headers = {
        'Authorization':f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'message': message
    }
    requests.request(method='POST',url = url,data = data,headers=headers)
    # debug
    # print(res)