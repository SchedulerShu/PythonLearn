import json

import requests




r = requests.get('http://cuiqingcai.com')
print (type(r))
print (r.status_code)
print (r.encoding)
# print r.text
print (r.cookies)

print("-----------------------基本请求-------------------------------------")
#requests库提供了http所有的基本请求方式。例如：

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
print (r.url)



print("-----------------------基本GET请求-------------------------------------")

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print (r.url)

#例如自己写一个JSON文件命名为a.json，内容如下
r = requests.get("a.json")
print (r.text)
print (r.json())

#如果想添加 headers，可以传 headers 参数
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print (r.url)



print("-----------------------基本POST请求-------------------------------------")
#对于 POST 请求来说，我们一般需要为它增加一些参数。那么最基本的传参方法可以利用 data 这个参数。
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print (r.text)
'''
有时候我们需要传送的信息不是表单形式的，需要我们传JSON格式的数据过去，所以我们可以用 json.dumps() 方法把表单数据序列化。

'''
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print (r.text)

'''
如果想要上传文件，那么直接用 file 参数即可:
'''
url = 'http://httpbin.org/post'
files = {'file': open('ex1.py', 'rb')}
r = requests.post(url, files=files)
print (r.text)


'''
requests 是支持流式上传的，这允许你发送大的数据流或文件而无需先把它们读入内存。要使用流式上传，仅需为你的请求体提供一个类文件对象即可
'''
with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)


print("-----------------------Cookies-------------------------------------")
# 如果一个响应中包含了cookie，那么我们可以利用 cookies 变量来拿到

url = 'http://example.com'
r = requests.get(url)
# print (r.cookies)
# print (r.cookies['example_cookie_name'])



print("-----------------------超时配置-------------------------------------")
#可以利用 timeout 变量来配置最大请求时间
# requests.get('http://github.com', timeout=0.001)
# print (r.url)


print("-----------------------会话对象-------------------------------------")

requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print(r.text)

'''
很明显，这不在一个会话中，无法获取 cookies，那么在一些站点中，我们需要保持一个持久的会话怎么办呢？
就像用一个浏览器逛淘宝一样，在不同的选项卡之间跳转，这样其实就是建立了一个长久会话。
'''

#在这里我们请求了两次，一次是设置 cookies，一次是获得 cookies
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

s = requests.session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)


print("-----------------------SSL证书验证-------------------------------------")
#现在随处可见 https 开头的网站，Requests可以为HTTPS请求验证SSL证书，就像web浏览器一样。要想检查某个主机的SSL证书，你可以使用 verify 参数
#如果我们想跳过刚才 12306 的证书验证，把 verify 设置为 False 即可 ,在默认情况下 verify 是 True，所以如果需要的话，需要手动设置下这个变量。
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
# print (r.text)


r = requests.get('https://github.com', verify=True)
# print (r.text)



print("-----------------------代理-------------------------------------")
#如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print (r.text)