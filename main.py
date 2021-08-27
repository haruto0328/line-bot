from flask import Flask, request, abort
import os
import psycopg2
import datetime
import pytz
import re

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction, PostbackEvent
)

app = Flask(__name__)

line_bot_api = LineBotApi("MessagingAPIのチャネルアクセストークン")
handler = WebhookHandler("MessagingAPIのチャネルシークレット")

## 1 ##
#Webhookからのリクエストをチェックします。
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得します。
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得します。
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    # # 署名を検証し、問題なければhandleに定義されている関数を呼び出す。
    try:
        handler.handle(body, signature)
# 署名検証で失敗した場合、例外を出す。
    except InvalidSignatureError:
        abort(400)
# handleの処理を終えればOK
    return 'OK'


now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
today = re.search('\d+-\d+-\d+', str(now)).group()

date_picker = TemplateSendMessage(
            alt_text='次回活動日時を設定してください',
            template=ButtonsTemplate(
                text='次回活動日時を設定してください。',
                title='次回活動日時を設定',
                actions=[
                    DatetimePickerTemplateAction(
                        label='設定',
                        data='action=buy&itemid=1',
                        mode='datetime',
                        initial=today+'t09:00',
                        min='2021-04-01t00:00',
                        max='2099-12-31t23:59'
                    )
                ]
            )
        )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text in ['次回の活動予定を設定']:
        line_bot_api.reply_message(
            event.reply_token,
            date_picker) #ここで予定日設定用のメッセージを返します。

@handler.default()
def default(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.postback.params['datetime'] + 'に活動予定日を設定しました。'))

    # データベースに次回活動予定日データを挿入
    conn = psycopg2.connect("host=" + "hogehoge" +
                            " port=" + "hogehoge" +
                            " dbname=" + "hogehoge" +
                            " user=" + "hogehoge" +
                            " password=" + "hogehoge")
    c = conn.cursor()
    c.execute("INSERT INTO datetimes (dates) VALUES ('"+event.postback.params['datetime']+"');")
    conn.commit()
    conn.close()


# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
