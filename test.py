# from bs4 import BeautifulSoup as BS

# file = open('index.html', 'r', encoding='utf-8')

# html = file.read()

# soup = BS(html, 'html.parser')

# main = soup.find('div', class_= 'main')
# navigator = main.find('div', class_= 'navigator')
# menu = navigator.find('ul', class_='menu')
# li = menu.find_all('li')
# for item in li:
#     print(item.text)


# дз

from bs4 import BeautifulSoup as BS

file = open('index.html', 'r', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

main = soup.find('div', class_= 'main')
content_wrapper = main.find('div', class_='content_wrapper')
post = content_wrapper.find_all('div', class_='post')
for item in post:
    print(item.text)
# h1 = post.find_all('h1', class_='title')
# print(h1)
# for item in h1:
#     print(item.text)

footer_box = main.find('div', class_='footer_box')
box = footer_box.find_all('div', class_='box')
# p = box.find_all('p')
for item in box:
    print(item.text.strip())




