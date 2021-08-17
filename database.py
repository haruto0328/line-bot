from main import default
import psycopg2
from datetime import datetime
import datetime
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

# c.execute("INSERT INTO dates VALUES ('2021-08-12T09:00')")

for row in c.execute('SELECT dates FROM datetimes ORDER BY id DESC LIMIT 1;'):
    plan = re.search('\d+-\d+-\d+', str(row)).group()
    today = str(datetime.date.today())
    if(plan == today):
        @handler.default()
        def default():
            # line_bot_api.reply_message(
            #     event.reply_token,
                TextSendMessage(text='今日の時から、活動があります。忘れずに参加してください！！'))

conn.close()