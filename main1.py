from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def main(url, HUB,  **kwargs):
    html = requests.get(url, **kwargs)
    soup = BeautifulSoup(html.text, 'html.parser') # Создали объект, выбрали парсер
    article = soup.find_all('article') # Получаем все статьи со страницы
    for art in article:
        dates = art.find_all(class_='tm-article-snippet__datetime-published') # Задаем классы в статьях, в которых мы ищем нужные эелементы
        titles = art.find_all(class_='tm-article-snippet__title-link')
        hrefs = art.find_all(class_='tm-article-snippet__readmore')
        prewiew = art.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        hubs = [hub.text.strip() for hub in prewiew]
        for hub in hubs:
            element_hub = hub.split(' ')
            for element_HUB in HUB:
                if element_HUB in element_hub:
                    date_ = [date.get_text() for date in dates]
                    print(''.join(date_))
                    title_ = [title.get_text() for title in titles]
                    print(''.join(title_))
                    href_ = [href.get('href') for href in hrefs]
                    print(f"https://habr.com{''.join(href_)}")
                    print('\n')


if __name__=='__main__':
    url = "https://habr.com/ru"
    HUB = ['IT', 'CSS-запросы', '2007', 'RAD']
    main(url, HUB, headers = {'User-Agent': UserAgent().chrome})