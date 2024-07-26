import requests
from bs4 import BeautifulSoup as BS
import openpyxl

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BS(html, 'html.parser')
    links = []
    main_content = soup.find('div', class_='main-content')
    grid_product = main_content.find('div', class_='grid-product')
    posts = grid_product.find_all('div', class_='col-6 col-lg-3')
    for post in posts:
        title = post.find('div', class_='product-title')
        price = post.find('div', class_='product-price product-price2').text.strip()
        product_art = post.find('div', class_='product-art').text.strip()
        # print(f'{title[0:20]} - {price} - {product_art}') 
        link = title.find('a').get('href')
        full_link = 'https://max.kg' + link
        links.append(full_link)
        print(full_link)
    return links


def get_posts(html):
    soup = BS(html, 'html.parser')
    
    main_content = soup.find('div', class_='main-content product-detail')
    price = main_content.find('div', class_='sum-price').text.strip()
    articul = main_content.find('span', class_='rounded product-art').text.strip()
    title = main_content.find('div', class_='d-flex align-items-center flex-wrap').find('h1').text.strip()
    try:
        brand = main_content.find('div', class_='product-title').find('p', class_='product-brand').text.strip()
    except:
        None
    description = main_content.find('div', class_='text-desc').text.strip()
    # print(f'- {title[0:20]}\n- Цена: {price}\n- {articul}\n- {brand}\n- Описание: {description[0:50]}\n\n')
    try:
        table = main_content.find('tr').text.strip()
        # print(table.text.strip())
    except:
        "У поста нет таблицы характеристик"
        
    data = {
        'title': title[0:30],
        'price': price,
        'articul': articul,
        'brand': brand,
        'description': description[0:100],
        # 'table': table
    }
    return data

def get_last_page(html):
    soup = BS(html, 'html.parser')
    main_content = soup.find('div', class_='main-content')
    pagination = main_content.find('div', class_='wrap-pagination')
    li = pagination.find('li', class_='last')
    last_page = li.find('a').get('data-page')
    return int(last_page)


def save_to_excel(data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Название'
    sheet['B1'] = 'Цена'
    sheet['C1'] = 'Артикул'
    sheet['D1'] = 'Бренд'
    sheet['E1'] = 'Описание'
    # sheet['F1'] = 'Характеристики'

    
    for i,item in enumerate(data,2):
        sheet[f'A{i}'] = item['title']
        sheet[f'B{i}'] = item['price']
        sheet[f'C{i}'] = item['articul']
        sheet[f'D{i}'] = item['brand']
        sheet[f'E{i}'] = item['description']
        # sheet[f'F{i}'] = item['table']
        
    wb.save('products.xlsx')

def main():
    URL = 'https://max.kg/catalog/komputery-i-noutbuki-planshety/noutbuki'
    html = get_html(URL)
    last_page = get_last_page(html)

    for i in range(1, 3):
        page_url = f'{URL}?page={i}'
        page = get_html(page_url)
        links = get_links(page)
        data = []
        for link in links:
            detail_html = get_html(link)
            data.append(get_posts(detail_html))
        save_to_excel(data)

if __name__ == '__main__':
    main()


