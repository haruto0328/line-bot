from main import default
import psycopg2
from datetime import datetime
import datetime
import pytz
import re

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import TextSendMessage


line_bot_api = LineBotApi("miP/OnH4rBYGo5qLlP7pyxAXFdss80DswDHNXqdafSxJ0nQZlKyfcwpHsyhN5FPYlk5Shc6WRo8aGBzIpdzknC2KueOtNbB4SIslsIKZdaprgn0Tf8qxxXBDEt9WV4h/lF/7tN0q1jpcQ7VcesfqHQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e157aafd232b4650558937ce7250f4d9")

conn = psycopg2.connect("host=" + "ec2-54-197-100-79.compute-1.amazonaws.com" +
                            " port=" + "5432" +
                            " dbname=" + "d469he2n9rkhus" +
                            " user=" + "epgqpirhombheu" +
                            " password=" + "24d6a2537ae752fc37baa19b3463e8e09c13732e60b26966afec049323e57c5e")

c = conn.cursor()
c.execute('SELECT dates FROM datetimes ORDER BY id DESC LIMIT 1')
for row in c:
    plan = re.search('\d+-\d+-\d+', str(row)).group()
    plan_time = re.search('\d+:\d+', str(row)).group()
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    today = re.search('\d+-\d+-\d+', str(now)).group()
    if(plan == today):
        line_bot_api.push_message('C3f419c10ffe995b0cc76e8cffbd14e09', messages=TextSendMessage(text='今日の'+plan_time+'から、活動があります。忘れずに参加してください！！'))

conn.close()