import requests
from bs4 import BeautifulSoup
import random


def getPCS(usertext):
    content = ''
    pcs_kind = ['剪刀','石頭','布']
    bot = random.randint(0,2)
    user_pcs = -1

    if usertext.find('石頭') != -1:
        user_pcs = 1
    elif usertext.find('剪刀') != -1:
        user_pcs = 0
    elif usertext.find('布') != -1:
        user_pcs = 2
    else:
        return '快點猜拳吧~'

    if user_pcs == bot:
        content = '你出了{}，我出了{}，我們好像平手喔'.format(pcs_kind[user_pcs],pcs_kind[bot])
    elif bot-user_pcs == 1 or bot-user_pcs == -2:
        content = '你出了{}，我出了{}，我贏了，再接再厲吧'.format(pcs_kind[user_pcs],pcs_kind[bot])
    else:
        content = '你出了{}，我出了{}，恭喜獲勝!'.format(pcs_kind[user_pcs],pcs_kind[bot])
    return content

def getSpeciall():
    content = ''
    head = 'https://cn.pornhub.com'
    rs = requests.get(head)
    soup = BeautifulSoup(rs.text,'html.parser')
    title = soup.select(".title > a")
    i=0
    res = []
    for x in title:
        i += 1
        link =  str(head+x.get('href'))
        title = str(x.get('title'))
        if link.find('view_video.php?') != -1:
            res.append(f'{title}\n{link}\n')
    sample = random.choices(res,k=10)
    print(sample)
    return ''.join(sample)

def getNews():
    content = ''
    head = 'https://www.bbc.com'
    rs = requests.get('https://www.bbc.com/zhongwen/trad/world')
    soup = BeautifulSoup(rs.text,'html.parser')
    title = soup.select('a > h3 > span')
    link = soup.select('div[class="eagle-item__body"] > a')
    for i in range(0,len(title)):
        content += title[i].string + '\n'
        content += head + link[i].get('href') + '\n'
        if i > 10:
            break
    return content
# 設定你接收訊息的網址，如 https://YOURAPP.herokuapp.com/callback


def getTrash():
    trash = ['願意接受像X光的審查，不要把我假釋，把我關到死。'
            ,'如果我貪污，一天給我一頓飯就好，我沒資格吃三頓飯。'
                ,'我跟你談大海，你跟我談浴缸？'
                ,'為什麼要不斷欺騙，為什麼要用邪門歪道？'
                ,'東西賣不出去，人進不來，民進黨執政怎麼發大財？'
                ,'知恥近乎勇！民進黨執政三年真的不行。'
                ,'天上最大的是玉皇大帝，最小的家裡旁邊的土地公，台灣最大的是總統，最小的是村里長。'
                ,'看看我們的空污，中部人的肺都快爆炸了！'
                ,'我的年紀大了，我的來日無多，這代人很快就會凋謝。'
                ,'.每一個心裡都覺得好悶，像全民大悶鍋一樣。'
                ,'民進黨前副總統呂秀蓮怎麼講民進黨？已經墮落了。韓國瑜是我爸媽取的，民主進步黨誰取的？前立法委員林正杰，他也看不下去。'
                ,'蔡英文用納稅人建立網軍，居然拿網軍的黑資料攻擊我韓國瑜，妳當網軍是吃到飽嗎？到處都要吃？'
                ,'我們總統被架空，因為被架空，所以很多狀況外，放縱派系，真的是吃台灣人肉，喝台灣人血，大撈特撈、大貪特貪，然後所有責任由蔡英文一個人扛。']  
    return trash[random.randrange(len(trash))]  


def getHelper():
    place = [
            '高雄市政府民政局'
            ,'高雄市政府財政局'
            ,'高雄市政府教育局'
            ,'高雄市政府經濟發展局'
            , '高雄市政府海洋局'
            ,'高雄市政府農業局'
            ,'高雄市政府觀光局'
            ,'高雄市政府都市發展局'
            ,'高雄市政府衛生局'
            ,'高雄市政府水利局'
            ,'高雄市政府社會局'
            ,'高雄市政府勞工局'
            ,'高雄市政府工務局'
            ,'高雄市政府警察局'
            ,'高雄市政府消防局'
            ,'高雄市政府文化局'
            ,'高雄市政府交通局'
            ,'高雄市政府環境保護局'
            ,'高雄市政府捷運工程局'
            ,'高雄市政府法制局'
            ,'高雄市政府地政局'
            ,'高雄市政府新聞局'
            ,'高雄市政府毒品防制局'
            ,'高雄市政府運動發展局'
            ,'高雄市政府青年局']
    return '這個我們請' + place[random.randrange(0,len(place))] +'局長發言，謝謝'
    