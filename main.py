from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
)

app = Flask(__name__)

#環境変数取得
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["tOliNdhJrc765XxCGItThMYGSistgj6GOnqdj3jUu1AcZi9Zz+vVTkOPX5kRnm/KcWfxDupseVXoDUkNlLS5PQsSW9v4hcZWSaEPTJsX4Hm7Rp2Y6WuG7yJe8X/fn2x7XOtlQw3CEsXjZy6unp50BgdB04t89/1O/w1cDnyilFU="]
# YOUR_CHANNEL_SECRET = os.environ["8ea6154ec5c4507837f28fc5b194c2c7"]

line_bot_api = LineBotApi("miP/OnH4rBYGo5qLlP7pyxAXFdss80DswDHNXqdafSxJ0nQZlKyfcwpHsyhN5FPYlk5Shc6WRo8aGBzIpdzknC2KueOtNbB4SIslsIKZdaprgn0Tf8qxxXBDEt9WV4h/lF/7tN0q1jpcQ7VcesfqHQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e157aafd232b4650558937ce7250f4d9")

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
 
## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。

date_picker = TemplateSendMessage(
            alt_text='予定日を設定',
            template=ButtonsTemplate(
                text='予定日を設定',
                title='YYYY-MM-dd',
                actions=[
                    DatetimePickerTemplateAction(
                        label='設定',
                        data='action=buy&itemid=1',
                        mode='date',
                        initial='2017-04-01',
                        min='2017-04-01',
                        max='2099-12-31'
                    )
                ]
            )
        )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        date_picker) #ここでオウム返しのメッセージを返します。

# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)