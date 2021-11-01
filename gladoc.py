# -*- coding: utf8 -*-
import requests
import json
import config
import datetime
from wxpusher import WxPusherTest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cookie = config.GLADOC_CONFIG['cookie']
wx = WxPusherTest()
contentType = 2
topicIds = ['2431']
url = 'https://glados.rocks/console/checkin'


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload = {
        'token': 'glados_network'
    }
    checkin = requests.post(url,
                            headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent,
                                     'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload),
                            verify=False)
    state = requests.get(url2,
                         headers={'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent},
                         verify=False)
    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        content = mess + '，you have ' + time + ' days left'
        summary = '[GladDoc签到消息] ' + str(datetime.datetime.now()) + ' ' + mess + '，you have ' + time + ' days left'

        wx.sendMessage(content, summary, contentType, topicIds, url)
        print(summary)
        return 1
    else:
        wx.sendMessage('[GladDoc签到消息] cookie过期', '[GladDoc签到消息] cookie过期', contentType, topicIds, url)
        print('[GladDoc签到消息] cookie过期')
        return 0


if __name__ == '__main__':
    start()
