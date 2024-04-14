from gpiozero import InputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import datetime
import sqlite3

# センサーのピン設定
PIN_SR501 = 4
# 取得間隔
INTERVAL_TIME = 1.0

# ピンを入力に設定(プルダウン設定)
factory = PiGPIOFactory()
sr501 = InputDevice(PIN_SR501, pull_up=False, pin_factory=factory)

try:
     while True:
          if sr501.is_active:
               db_connect = sqlite3.connect('/home/nakamura0067/workspace/death-notice/sqlite_test.db')
               db_curs = db_connect.cursor()
               dt_now = datetime.datetime.now() 
               sql = 'INSERT INTO human_sensor(high_date) values ("' + dt_now.strftime('%Y/%m/%d %H:%M') + '")'
               db_curs.execute(sql)
               db_connect.commit()
               db_connect.close()
          sleep(INTERVAL_TIME)
except KeyboardInterrupt:
     print("stop")
