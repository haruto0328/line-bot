import sqlite3
from datetime import datetime
import datetime
import re

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import TextSendMessage


line_bot_api = LineBotApi("miP/OnH4rBYGo5qLlP7pyxAXFdss80DswDHNXqdafSxJ0nQZlKyfcwpHsyhN5FPYlk5Shc6WRo8aGBzIpdzknC2KueOtNbB4SIslsIKZdaprgn0Tf8qxxXBDEt9WV4h/lF/7tN0q1jpcQ7VcesfqHQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e157aafd232b4650558937ce7250f4d9")


conn = sqlite3.connect('iungoback.db')
c = conn.cursor()

# c.execute("INSERT INTO dates VALUES ('2021-08-12T09:00')")

for row in c.execute('SELECT datetime FROM dates where rowid = last_insert_rowid()'):
    plan = re.search('\d+-\d+-\d+', str(row)).group()
    today = str(datetime.date.today())
    if(plan == today):
        # print('今日が活動日です。')
        def default(event):
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage('今日の時から、活動があります。忘れずに参加してください！！'))


# データベースへのアクセスが終わったら close する
conn.close()