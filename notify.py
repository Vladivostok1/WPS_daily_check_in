import json,requests
#发送通知
def post_push(token, title, content):
    url = 'http://pushplus.hxtrip.com/send'
    data = {
    "token": token,
    "title": title,
    "content": content
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)