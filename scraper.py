import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = []
    for item in soup.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'):
        title = item.text
        link = item.find_parent('a')['href']
        link = 'https://www.bbc.com' + link if link.startswith('/') else link
        news_list.append({'title': title, 'link': link})

    return news_list

# Example usage:
news_list = scrape_news()
print(news_list)
