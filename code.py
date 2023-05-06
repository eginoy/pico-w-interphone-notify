# screen /dev/tty.usb_name 115200
import os,board,analogio,time
import setupWifi
import apiClient

cnPool = setupWifi.run()

# ADC2(Raspberrypi Pico W GPIOピン34)の値を取得
adc2 = analogio.AnalogIn(board.A2)
notifySensorThreshold = os.getenv('NOTIFY_SENSOR_THRESHOLD')

# 起動時に一度LINEに通知を送る。(正しくネットワークに接続していることを確認するため)
apiClient.pushToLine(cnPool,'Raspberry Pi Pico Wが起動しました。')

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    time.sleep(1)
    v = get_voltage(adc2)
    print(v)
    if v > notifySensorThreshold:
      apiClient.pushToLine(cnPool,'インターホンが押されました')