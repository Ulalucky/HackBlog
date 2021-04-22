import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_dates(html):
    soup = BeautifulSoup(html, 'lxml')
    get_main_div = soup.find('div', class_="blog-posts clear")
    return get_main_div


def get_every_date(html):
    news_hack = html.find_all('div', class_='clear home-post-box cf')
    list_auto = []
    for hack in news_hack:
        try:
            photo = hack.find('img', class_="home-img-src lazyload").get('data-src')
        except:
            photo = ""
        try:
            title = hack.find('h2', class_='home-title').text
        except:
            title = ''

        data = {'title': title.replace('\n', '').strip(),
                'photo': photo}
        list_auto.append(data)
    return list_auto


def pars():
    url = 'https://thehackernews.com/search/label/Cyber%20Attack'
    html = get_html(url)
    html = get_dates(html)
    list_ = get_every_date(html)
    return list_