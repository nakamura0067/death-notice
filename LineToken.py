import requests
import datetime
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

db_connect = sqlite3.connect('sqlite_test.db')
db_curs = db_connect.cursor()

dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')

# データ参照の命令をSQLにて指示
sql = 'SELECT * FROM human_sensor where high_date = "'+ dt_now + '"'
db_curs.execute(sql)
human_sensor_count = db_curs.fetchone()

if human_sensor_count is None:
     sql = 'INSERT INTO human_sensor(high_date) values ("' + dt_now + '")'
     db_curs.execute(sql)

db_connect.commit()
db_connect.close()

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
data = {"message": "私は死んだ！\n↓この時にはだいたい死んでる\n" + dt_now}

requests.post(
     "https://notify-api.line.me/api/notify",
     headers=headers,
     data=data,
)