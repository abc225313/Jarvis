from flask import Flask, request, abort
from bs4 import BeautifulSoup
import requests


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def function(text):
    if(text=='未來天氣'):
        res = requests.get('https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW')
        soup = BeautifulSoup(res.text,'html.parser')
        tag_name = 'tbody tr td'
        art = soup.select(tag_name)
        text = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[9].text+'\n'+'溫度:'+art[11].text+'      '+'降雨機率:'+art[13].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[17].text+'\n'+'溫度:'+art[19].text+'     '+'降雨機率:'+art[21].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[25].text+'\n'+'溫度:'+art[27].text+'     '+'降雨機率:'+art[29].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[33].text+'\n'+'溫度:'+art[35].text+'     '+'降雨機率:'+art[37].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
             CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[41].text+'\n'+'溫度:'+art[43].text+'     '+'降雨機率:'+art[45].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
             CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[49].text+'\n'+'溫度:'+art[51].text+'     '+'降雨機率:'+art[53].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
             CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[57].text+'\n'+'溫度:'+art[59].text+'     '+'降雨機率:'+art[61].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
              CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[65].text+'\n'+'溫度:'+art[67].text+'     '+'降雨機率:'+art[69].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
               CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[73].text+'\n'+'溫度:'+art[75].text+'     '+'降雨機率:'+art[77].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            ),
                CarouselColumn(
                thumbnail_image_url='https://news.pts.org.tw/news_images/388570/1521266509q.jpg',
                title='文化大學未來天氣',
                text='未來時間:'+art[81].text+'\n'+'溫度:'+art[83].text+'     '+'降雨機率:'+art[85].text,
                actions=[
                    URITemplateAction(
                        label='資料來源',
                        uri='https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW'
                    )
                ]
            )

        ]
    )
)
    else:
        return catch(text)

    return text




def catch(text):
    if text=='10':
        x=9
        y=11
        z=13
        
    elif text=='20':
        x=17
        y=19
        z=21
        
    elif text=='30':
        x=25
        y=27
        z=29
    elif text=='40':
        x=33
        y=35
        z=37
    elif text=='50':
        x=41
        y=43
        z=45
    elif text=='60':
        x=49
        y=51
        z=53

    elif text=='70':
        x=57
        y=59
        z=61
    elif text=='80':
        x=65
        y=67
        z=69
    elif text=='90':
        x=73
        y=75
        z=77
    elif text=='100':
        x=81
        y=83
        z=85
    elif text=='110':
        x=89
        y=91
        z=93
    elif text=='120':
        x=97
        y=99
        z=101

    else:
        return TextSendMessage(text=nocatch(text))

    res = requests.get('https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW')
    soup = BeautifulSoup(res.text,'html.parser')
    tag_name = 'tbody tr td'
    art = soup.select(tag_name) 
    text = '未來時間:'+art[x].text+'\n'+'溫度:'+art[y].text+'\n'+'降雨機率:'+art[z].text
    return TextSendMessage(text = text)


def nocatch(text):
    
    if (text.find('陳冠霖')!=-1):
        text = '開發我的天才'


    elif (text.find('鄭人豪')!=-1):
        text = '你才是彩蛋!'
        

    elif(text.find('王麒霖')!=-1):
        text = '趕快去學程式語言!!'
        


    elif(text.find('關鍵字')!=-1):
        text = '關鍵字要靠心去找!!'
       


    elif(text.find('賈維斯')!=-1):
        text = '我是被開發機初號...算成功的話'
        


    elif(text.find('火影忍者')!=-1):
        text = '你也知道開發者喜歡喔~'
       

    elif(text.find('張聖彪')!=-1):
        text = '좋은 친구^ ^'


    elif(text.find('小傑')!=-1):
        text = '他是我的死對頭'


    elif text=='天氣資訊':
        text = '請輸入代號日後可直接輸入代碼'+'\n'+'台北天氣(捷運劍潭站):1'+'\n'+'文化大學:2'+'\n'+'擎天崗:3'



    elif text=='未來天氣':
        text = '輸入30為3小時'+'\n'+'40為4小時'+'\n'+'以此類推最多至12小時'+'\n'+'日後能直接輸入'

            

    elif text=='抽一句話':
        import random
        text = random.choice(['嗨你好,我是賈維斯','公車部分因為技術問題取消了','目前我是以天氣為主打的機器人','猜猜關鍵字~','創作者最愛看的動漫是?','開發者的名字是?'
    ,'開發者的好兄弟是?','加油 有夢最美 失望相隨(開玩笑的','其實我是真人....','我的鋼鐵衣呢!!','開發者不叫小勞勃道尼喔','我的電力來源是愛','我躺在雲端有時會太舒服會遲緩一下'
    ,'做著做著就成功了,想著想著就失敗了','天下無難事 只怕有心人','我測量溫度時都是站在太陽底下','有時開發者會優化一下 所以不能動是正常的 哭哭','放棄前都不叫失敗','安安','。'
    ,'傳送意見這功能 是不會主動傳達給我 除非我去特地檢查且一過12點資訊就會不見~','若有意見想給我 可以Gmail我喔 abc225313@gmail.com','!!!','掰掰','此用戶已將您封鎖','。。。'
    ,'無言','有話直說 說到做到','添加新選項做與不做 只要輸入?即可'])
        


    elif text=='傳送意見':
        text='任何想對我說的話 只要前面+s就能傳送囉 ex: S(大寫)開發者好帥\n或者這是我的g-mail:abc225313@gmail.com\n通常傳送的訊息雲端會自動刷掉,建議寫信'


    elif text=='1':
        res = requests.get('https://weather.com/zh-TW/weather/hourbyhour/l/TWXX3586:1:TW')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        tag_name = 'tbody tr td'
        art = soup.select(tag_name) 
        text = '溫度:'+art[3].text+'\n'+'降雨機率:'+art[5].text




    elif text=='2':
        res = requests.get('https://weather.com/zh-TW/weather/hourbyhour/l/TWXX6190:1:TW')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        tag_name = 'tbody tr td'
        art = soup.select(tag_name) 
        text = '溫度:'+art[3].text+'\n'+'降雨機率:'+art[5].text


    

    elif text=='3':
        res = requests.get('https://weather.com/zh-TW/weather/hourbyhour/l/TWXX5781:1:TW')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        tag_name = 'tbody tr td'
        art = soup.select(tag_name)
        text='測量時間:'+art[1].text+'\n'+'溫度:'+art[3].text+'\n'+'降雨機率:'+art[5].text



    elif (text.find('S')!=-1):
        fp = open("message.text", "a")
        text =text.strip('S')
        fp.write(text+',\n')
        text='傳送成功 '


    

    elif text=='311':
        fp = open("message.text", "r")
        send=fp.read()
        return send
 

    elif text=='427':
        fp =open("message.text","w")
        fp.truncate()
        text='成功了'

    

    elif text == '美金匯率':
        res = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        tag_name = 'tbody tr td'
        art = soup.select(tag_name)
        art = art[4].text         
        text = '美金現在'+art+'元'


    elif text=='？'or text=='?':
        import random
        text=random.choice(['做','不做'])


    else:
        text='找些關鍵字吧~有時我會在維修中請見諒'


    return text
       
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message=function(event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
