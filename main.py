from django.http import HttpResponse
from linebot import LineBotApi, WebhookParser
from linebot.models import TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction

line_bot_api = LineBotApi('miP/OnH4rBYGo5qLlP7pyxAXFdss80DswDHNXqdafSxJ0nQZlKyfcwpHsyhN5FPYlk5Shc6WRo8aGBzIpdzknC2KueOtNbB4SIslsIKZdaprgn0Tf8qxxXBDEt9WV4h/lF/7tN0q1jpcQ7VcesfqHQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('e157aafd232b4650558937ce7250f4d')


def webhook(events):
    # Signatureチェック等

    for event in events:
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

        line_bot_api.reply_message(
            event.reply_token,
            date_picker
        )

    return HttpResponse()