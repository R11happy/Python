from bs4 import BeautifulSoup
info = []
with open('G:/Python_Code/Crowler4Week/week1/1_2/web/new_index.html', 'r')as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info ')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')

# 将标签全部放入字典中，方便查询
for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
    data = {
        'title':title.get_text(),
        'rate':rate.get_text(),
        'desc':desc.get_text(),
        'cate':list(cate.stripped_strings),
        'image':image.get('src')    #获得标签中属性用get方法
    }
    info.append(data)

# 筛选出大于3分的文章
for i in info:
    if float(i['rate'])> 3:
        print(i['title'], i['cate'])
    # body > div.main - content > ul > li: nth - child(1) > img
    # body > div.main - content > ul > li: nth - child(1) > div.article - info > h3 > a
    # body > div.main - content > ul > li: nth - child(1) > div.article - info > p.meta - info > span:nth - child(2)
    # body > div.main - content > ul > li: nth - child(1) > div.article - info > p.description
    # body > div.main-content > ul > li:nth-child(1) > div.rate > span