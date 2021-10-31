import requests
import json
import config


class WxPusherTest:
    def sendMessage(self, content, summary, contentType, topicIds, url):
        headers = {'Content-Type': 'application/json'}
        data = {
            "appToken": config.WXPUSHER_CONFIG['appToken'],
            "content": content,
            "summary": summary,
            "contentType": contentType,
            "topicIds": topicIds,
            "url": url
        }
        response = requests.post(url=config.WXPUSHER_CONFIG['url'], headers=headers,
                                 data=json.dumps(data))
        print(response.text)
        return response

# if __name__ == '__main__':
#     wx = WxPusherTest()
#     rst = wx.sendMessage('123', '12344', 2, ['2431'], 'https://blog.csdn.net/weixin_43064185/article/details/102454649')
#     print(rst.text)