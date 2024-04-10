import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

dt_now = datetime.datetime.now()
data = {"message": "\n現在の時間は" + dt_now.strftime('%Y年%m月%d日 %H:%M:%S') + "です。"}

requests.post(
     "https://notify-api.line.me/api/notify",
     headers=headers,
     data=data,
)