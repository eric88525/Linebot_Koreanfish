# encoding: utf-8
from flask import Flask, request, abort
from function import *
import random
from config import line_token,line_secret


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


app = Flask(__name__)

# 填入你的 message api 資訊
line_bot_api = LineBotApi(line_token)
handler = WebhookHandler(line_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage )
def handle_message(event):

    print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    usertext = event.message.text
    content = 'xxx'
    # 讓市長學習
    if usertext.find('市長學') != -1:
        content = writeDB(usertext)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 

    elif usertext.find('市長') == -1 and usertext.find('國瑜') == -1:
        return
    elif usertext.find('特別服務') !=-1:
        content = getSpeciall()
    elif usertext.find('猜拳') is not -1:
        content = getPCS(usertext)
    elif usertext.find('新聞') is not -1:
        content = getNews()
    elif usertext.find('幹話') != -1:
        content = getTrash()

    else: # 搜資料庫
        content = getDB(usertext)
        
    if content == 'xxx':
        return 
     
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))

import os
if __name__ == "__main__":
    # BUILD DB & TABLE
    app.run(host='0.0.0.0',port=os.environ['PORT'])