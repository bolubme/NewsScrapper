import requests
from bs4 import BeautifulSoup
from urlFile import bbcUrl


def scrape():
    for url in bbcUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for headline in soup.find_all('a', class_='gs-c-promo-heading'):
            headline_text = headline.find('h3').text
            headline_path = headline['href']
            print(headline_text)

            if 'https://www.bbc.co.uk' in headline_path or 'http://www.bbc.co.uk' in headline_path:
                headline_link = headline_path
            else:
                headline_link = f'https://www.bbc.co.uk{headline_path}'

            print(headline_link)
            if '/live/' in headline_link.lower():
                continue

            # Scraping individual article page
            article_response = requests.get(headline_link, headers={'User-Agent': 'Mozilla/5.0'})
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            article_div = article_soup.find_all("div", {"data-component": "text-block"})
            temp_article = ""
            for div in article_div:
                p = div.find("p")
                if p:
                    text = p.get_text()
                    if 'click here' not in text.lower():
                        temp_article += "\n" + text.strip()
            if temp_article:
                print("Article Content")
                print(temp_article)

                # Scraping image from article page
                article_images = article_soup.find_all('div', class_='ssrcss-ab5fd8-StyledFigureContainer')
                for image in article_images:
                    img_tag = image.find('img')
                    if img_tag:
                        img_src = img_tag['src']
                        print("IMAGE PRINTING")
                        print(img_src)



