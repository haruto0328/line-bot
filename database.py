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


line_bot_api = LineBotApi("MessagingAPIのチャネルアクセストークン")
handler = WebhookHandler("MessagingAPIのチャネルシークレット")

conn = psycopg2.connect("host=" + "hogehoge" +
                            " port=" + "hogehoge" +
                            " dbname=" + "hogehoge" +
                            " user=" + "hogehoge" +
                            " password=" + "hogehoge")

c = conn.cursor()
c.execute('SELECT dates FROM datetimes ORDER BY id DESC LIMIT 1')
for row in c:
    plan = re.search('\d+-\d+-\d+', str(row)).group()
    plan_time = re.search('\d+:\d+', str(row)).group()
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    today = re.search('\d+-\d+-\d+', str(now)).group()
    if(plan == today):
        line_bot_api.push_message('LINEグループID', messages=TextSendMessage(text='今日の'+plan_time+'から、活動があります。忘れずに参加してください！！'))

conn.close()
