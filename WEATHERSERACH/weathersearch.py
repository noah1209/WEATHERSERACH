import ui
import requests
import time
import datetime
from PIL import Image
import json
import time
import geocoder
text = ""
a = ""
b = ""
c = ""


def button_tapped(sender):
    sender.title = 'Searching'
    print("緯度,経度")
    print(c + ',' + b)
    v.close()


def copy(sender):
    text = sender.superview['textfield1'].text
    str2 = "{}".format(text)
    dt_now = datetime.datetime.now()
    print(dt_now)
    hour = dt_now.hour
    minute = dt_now.minute
    if (hour > 19) or (hour <= 5):
        print("こんばんは。")
    elif (hour > 11):
        print("こんにちは。")
    elif (hour > 5):
        print("おはようございます。")
    print("今のお天気をお知らせします")
    str1 = "ただいまの時刻は{}時{}分です。".format(hour, minute)
    print(str1)
    ret = geocoder.osm(str2, timeout=5.0)
    global c
    global b
    global a
 # 緯度と経度を地点から取得
    c = str(ret.latlng[0])
    b = str(ret.latlng[1])
    API_KEY = "4fa2fe87026af58a0ae452080a60b3d6"
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# それをURLに代入
    url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={key}"
    url1 = url.format(lat=c, lon=b, key=API_KEY)
    response = requests.get(url1)

    data = response.json()
    jsontext = json.dumps(data, indent=4)
    f = open('Now.json', 'w', encoding='UTF-8')

    f.write(jsontext)

    f.close()
    print(str2+"は")
    rtn = "01n" in jsontext
    if (rtn == True):
        print("快晴です。夜空がよく見えるでしょう")
        a = 1
    rtn = "02n" in jsontext
    if (rtn == True):

        print("少し雲がかかっています。")
        a = 2
    rtn = "03n" in jsontext
    if (rtn == True):
        print("曇りです。")
        a = 3
    rtn = "04n" in jsontext
    if (rtn == True):
        print("雲がかかっています。")
        a = 5
    rtn = "09n" in jsontext
    if (rtn == True):
        print("雨雲がかかっていて少し雨が降っています。")
        a = 6
    rtn = "010n" in jsontext
    if (rtn == True):
        print("雨が降っています。")
        a = 7
    rtn = "011n" in jsontext
    if (rtn == True):
        print("雷雨です。ところにより雷が落ちるので気をつけてください。")
    a = 8
    rtn = "30n" in jsontext
    if (rtn == True):
        print("雪が降っています。")
        a = 9
    rtn = "50n" in jsontext
    if (rtn == True):
        print("霧がかかっています。")
        a = 10
    rtn = "01d" in jsontext
    if (rtn == True):
        print("快晴です。")
        a = 11
    rtn = "02d" in jsontext
    if (rtn == True):
        print("少し雲がかかっています。")
        a = 12
    rtn = "03d" in jsontext
    if (rtn == True):
        print("曇りです。")
        a = 13
    rtn = "04d" in jsontext
    if (rtn == True):
        print("雲がかかっています。")
        a = 14
    rtn = "09d" in jsontext
    if (rtn == True):
        print("雨雲がかかっていて少し雨が降っています。")
        a = 15
    rtn = "010d" in jsontext
    if (rtn == True):
        print("雨が降っています。")
        a = 16
    rtn = "011d" in jsontext
    if (rtn == True):
        print("雷雨です。ところにより雷が落ちるので気をつけてください。")
        a = 17
    rtn = "30d" in jsontext
    if (rtn == True):
        print("雪が降っています。")
        a = 18
    rtn = "50d" in jsontext
    if (rtn == True):
        print("霧がかかっています。")
        a = 19
    f1 = open('Now.json', 'r', encoding='UTF-8')
    jsn = json.load(f1)
    w = jsn["main"]
    print()
    t = w['temp']
    p = w["pressure"]
    h = w["humidity"]
    t = 1.8 * t + 32 - 273.15 * 1.8
    t = ((t - 32)) / 1.8
    t = round(t, 1)
    str2 = "現在の気温は{}°C、気圧は{}hpaです。湿度は{}%でしょう。".format(t, p, h)
    print(str2)


v = ui.load_view('SERACH.pyui')
v['imageview1'].image = ui.Image('earth.JPG')
v.present('sheet')
