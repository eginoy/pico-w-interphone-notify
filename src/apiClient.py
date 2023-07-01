import os
import ssl
import microcontroller
import adafruit_requests

class notify:
  def __init__(self,socket):
    self.client = adafruit_requests.Session(socket,ssl.create_default_context())
  
  def requestTest(self):
    try:
      self.client.request(method='GET',url = 'https://www.google.com/');
    except:
      # 疎通確認できなければ再起動(ハードリセット)してシステムの回復を試みる。(起動時にネットワーク接続を行っているので)
      # https://learn.adafruit.com/circuitpython-essentials/circuitpython-resetting#hard-reset-3087083
      microcontroller.reset();

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