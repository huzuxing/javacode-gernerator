import requests

def post_request():
    params = {"deviceToken" : "123456", "appId":"appId", "serverId":"0", "openId":"openId"}
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',  'token': '61ea92ab32003afb44ab5f8'}
    url = "http://127.0.0.1:8094/collect/api/v1/app/token"
    req = requests.post(url, params, header_dict)
    print(req.text)
post_request()