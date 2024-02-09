import requests
from bs4 import BeautifulSoup
from urlFile import talksportUrl

def scrape():
    for url in talksportUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for headline in soup.find_all('a', class_='text-anchor-wrap'):
            headline_text = headline.find('h3', class_='teaser__subdeck').text.strip()
            headline_link = headline['href']

            print(headline_text)
            print(headline_link)

            # Scraping individual article page and images
            article_response = requests.get(headline_link, headers={'User-Agent': 'Mozilla/5.0'})
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            article_div = article_soup.find("div", class_='article__content')
            temp_article = ''
            if article_div:
                for p in article_div.find_all('p'):
                    text = p.get_text()
                    temp_article += "\n" + text

            if temp_article:
                # Extract article image
                article_image = article_soup.find("div", class_='article__media-img-container')
                if article_image:
                    image_src = article_image.find('img')['data-src']
                    print(image_src)
