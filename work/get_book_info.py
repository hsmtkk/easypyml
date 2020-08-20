import time

import requests
from bs4 import BeautifulSoup

def get_book_info(book_url):
    res = requests.get(book_url)
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    div_book_detail = soup.find('div', class_='block-book-detail')
    book_title = div_book_detail.find('h2')
    book_price = div_book_detail.find('p', class_='module-book-price')
    book_data = dict()
    dl_book_data = div_book_detail.find('dl', class_='module-book-data')
    for tag in dl_book_data.find_all(['dt', 'dd']):
        if tag.name == 'dt':
            key = tag.get_text()
        if tag.name == 'dd':
            book_data[key] = tag.get_text().strip()

    return [book_title.get_text(), book_price.get_text(), book_data['発売日'], book_data['著者']]

def demo1():
    info = get_book_info('https://book.impress.co.jp/books/1116101151')
    print(info)

def demo2():
    res = requests.get('https://book.impress.co.jp/booklist/')
    html_doc = res.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    div_book_list = soup.find('div', class_='block-book-list-body')
    book_urls = list()
    a_tags = div_book_list.find_all('a')
    for a_tag in a_tags:
        if not a_tag['href'] in book_urls:
            book_urls.append(a_tag['href'])

    book_info_list = list()
    for book_url in book_urls:
        print('scraping:', book_url)
        book_info_list.append(get_book_info(book_url))
        time.sleep(1)
    print('completed')

    with open('book_data.tsv', 'w', encoding='utf-8') as f:
        for book_info in book_info_list:
            f.write('\t'.join(book_info) + '\n')

if __name__ == '__main__':
    demo2()
