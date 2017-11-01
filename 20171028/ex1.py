from pyquery import PyQuery as pq
import requests
url = 'https://movie.douban.com/top250'
content = requests.get(url).text

for movie in pq(content).find('.info'):
    mov = pq(movie)
    title = mov.find('.title').html()
    score = mov.find('.rating_num').text()
    comment = mov.find('.quote').text()
    print (title)
    print ('  '+score+comment)

'''
肖申克的救赎
  9.6希望让人自由。
霸王别姬
  9.5风华绝代。
这个杀手不太冷
  9.4怪蜀黍和小萝莉不得不说的故事。
...............

'''

#-----------------------------------------------------------------------
