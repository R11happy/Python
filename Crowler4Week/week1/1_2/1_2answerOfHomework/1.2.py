from bs4 import BeautifulSoup
path = './1_2_homework_required/index.html'
with open(path, 'r')as web_data:
    Soup = BeautifulSoup(web_data, 'lxml')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    # print(titles, images, prices, stars, reviews, sep='\n---------\n')
for title, image, review, price, star in zip(titles, images, reviews, prices, stars):
    # for循环,把每个元素装到字典中
    data = {
        'title': title.get_text(),  #get_text()取出文本
        'image': image.get('src'),  #get方法取出带有src的图片链接
        'review': review.get_text(),
        'price' : price.get_text(),
        'star' : len(star.find_all("span", class_='glyphicon-star'))
        # 观察发现,每一个星星会有一次<span class="glyphicon glyphicon-star"></span>,所以我们统计有多少次,就知道有多少个星星了;
        # 使用find_all 统计有几处是★的样式,第一个参数定位标签名,第二个参数定位css 样式,具体可以参考BeautifulSoup 文档示例http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all;
        # 由于find_all()返回的结果是列表,我们再使用len()方法去计算列表中的元素个数,也就是星星的数量
    }
    print(data)
