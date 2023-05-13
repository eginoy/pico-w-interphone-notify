import os
import ssl
import adafruit_requests

class notify:
  def __init__(self,socket):
    self.client = adafruit_requests.Session(socket,ssl.create_default_context())
  
  def pushToLine(self,message):
    headers = {
        'Authorization':f'Bearer {os.getenv('LINE_TOKEN')}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'message': message
    }
    try:
      self.client.request(method='POST',url = 'https://notify-api.line.me/api/notify',data = data,headers=headers)
    except:
      pass