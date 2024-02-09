import requests
from bs4 import BeautifulSoup
from urlFile import independentUrl

def scrape():
    for url in independentUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for article in soup.find_all('div', class_='article-default'):
            headline = article.find('a', class_='title')
            if headline:
                headline_text = headline.text.strip()
                headline_link = headline['href']
                if '/vouchercodes/' in headline_link.lower():
                    continue

                print(f"Headline: {headline_text}")
                print(f"Link: https://www.independent.co.uk/{headline_link}")

                # Fetch article content
                article_response = requests.get(f"https://www.independent.co.uk/{headline_link}", headers={'User-Agent': 'Mozilla/5.0'})
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extract article content
                article_content = article_soup.find("div", id='main')
                if article_content:
                    for paragraph in article_content.find_all('p'):
                        print(paragraph.text)

                    # Extract article image
                    article_image = article_soup.find("meta", property="og:image")
                    if article_image:
                        print("Article Image:", article_image['content'])
                    else:
                        print("No article image found.")

                else:
                    print("No article content found.")

                print("\n")
            else:
                print("No headline found.")

