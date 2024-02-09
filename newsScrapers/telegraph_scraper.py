# telegraph_scraper.py
import requests
from bs4 import BeautifulSoup
import urllib.parse
from urlFile import telegraphUrl

def scrape():
    for url in telegraphUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for headline in soup.find_all('a', class_='list-headline__link u-clickable-area__link'):
            headline_text = headline.find('span', class_='list-headline__text').find('span').text
            headline_path = headline.get('href')

            # Constructing the complete URL for the article
            headline_link = urllib.parse.urljoin(url, headline_path)
            print("------------------------------------------------")
            print(headline_text)
            print(headline_link)

            # Scraping individual article page and images
            article_response = requests.get(headline_link, headers={'User-Agent': 'Mozilla/5.0'})
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            article_div = article_soup.find("div", {"data-js": "article-body"})
            if article_div:
                temp_article = ""
                for p in article_div.find_all("p"):
                    text = p.get_text()
                    temp_article += "\n" + text
                print(temp_article)

                # Extracting images with class .article-body-image__source
                images = article_div.find_all('img', class_='article-body-image__source')
                for image in images:
                    image_url = image.get('src')
                    image_main_url = f'https://www.telegraph.co.uk{image_url}'
                    print("IMAGE URL")
                    print(image_main_url)
                    # Add your code to handle the image URL here (e.g., save, download, etc.)
                print("------------------------------------------------")

            else:
                print("Article content not found.")
