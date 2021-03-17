from bs4 import BeautifulSoup
import urllib.request
url = 'https://www.coolmate.me/collection/ao-thun-cotton-compact?sort=created_at'
# url = 'https://www.coolmate.me/collection/phu-kien'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'html.parser')
# >>> new_feed = soup.find('div',class_='products-list').find('a')
# >>> title = new_feed.contents
# >>> img_t= soup.find('div',class_='products-list').find_all('img',class_=" lazyloaded")
# >>> for i in img_test:
# 	img = i.get('src')
# 	print(img)
# 	img_name= random.randrange(1,500)
# 	full_name = str(img_name) + ".png"
# 	urllib.request.urlretrieve(img, full_name)
# 	print("dont wait for luck!")

# ====
new_feed = soup.find('div',class_='products-list').find_all('div',class_='product__content')
for feed in new_feed:
	title = feed.find('a').contents
	prices = feed.find('span',class_ ='product__prices--regular').contents
	# print('Title: {0} - Prices {1}'.format(title,prices))
	print(title,prices)
	# print(prices)