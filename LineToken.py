import requests
import datetime
import os
import sqlite3
from dotenv import find_dotenv,load_dotenv

load_dotenv(find_dotenv())
ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

db_connect = sqlite3.connect('/home/nakamura0067/workspace/death-notice/sqlite_test.db')
db_curs = db_connect.cursor()

dt_now = datetime.datetime.now() 
dt_pre = dt_now + datetime.timedelta(days=-7)

# 一週間前のデータを取得する
sql = 'SELECT * FROM human_sensor where high_date > "'+ dt_pre.strftime('%Y/%m/%d') + '"'
db_curs.execute(sql)
human_sensor_list = db_curs.fetchall()

if human_sensor_list is None:
     headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
     data = {"message": "私は死んだ！\n↓この時にはだいたい死んでる\n" + dt_now.strftime('%Y/%m/%d %H:%M')}

     requests.post(
          "https://notify-api.line.me/api/notify",
          headers=headers,
          data=data,
     )
else:
     sql = 'INSERT INTO human_sensor(high_date) values ("' + dt_now.strftime('%Y/%m/%d %H:%M') + '")'
     db_curs.execute(sql)

db_connect.commit()
db_connect.close()
