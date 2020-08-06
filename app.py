# encoding: utf-8
from flask import Flask, request, abort
from enum import Enum
from function import getNews,getSpeciall,getTrash,getPCS,getHelper
import json
import sqlite3
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

class talkType(Enum):
    normal = 0
    notnormal = 1
    playgame = 2
    message = 3

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
        content = 'learn'
        insdata = str(usertext).split('@')
        if len(insdata) != 3 or insdata[0]!='市長學':

            #content = f'{str(insdata)},{len(insdata)},{type(insdata)},{insdata[0]}'
            content = '你到底想讓我學什麼呢'
        else:
            conn = sqlite3.connect('DB.db')
            sql_command = f"insert into kfish values ('{insdata[1]}','{insdata[2]}','{event.reply_token}')"
            cursor = conn.cursor()
            cursor.execute(sql_command)
            content = f'謝謝這位同學，市長學到了 {insdata[1]} : {insdata[2]}'
            conn.commit()
            conn.close()
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
        
        insdata = str(usertext).split(' ')

        if len(insdata) == 2 and insdata[0]=='市長':
            conn = sqlite3.connect('DB.db')
            cursor = conn.cursor()
            reply = cursor.execute(f"select answer from kfish where question = '{insdata[1]}'").fetchall()
            if len(reply):
                content = reply[random.randrange(0,len(reply))][0] 
            else:
                content = getHelper()
            conn.close()
    if content == 'xxx':
        return 
     
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))

import os
if __name__ == "__main__":
    # BUILD DB & TABLE
    app.run(host='0.0.0.0',port=os.environ['PORT'])