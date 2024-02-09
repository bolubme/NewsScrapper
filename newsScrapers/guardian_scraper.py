import requests
from bs4 import BeautifulSoup
from urlFile import guardianUrl


def scrape():
    for url in guardianUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for headlines in soup.find_all('div', class_="dcr-omk9hw"):
            headline = headlines.find('a', class_='dcr-lv2v9o')
            if headline:
                headline_text = headline.get('aria-label', '')  # Extract aria-label text
                headline_link = headline.get('href', '')  # Extract href link
                if '/live/' in headline_link.lower() or 'first thing:' in headline_text.lower() or '/crosswords/' in headline_link.lower():
                    continue

                # Fetch article content
                article_response = requests.get(f'https://www.theguardian.com/{headline_link}',
                                                headers={'User-Agent': 'Mozilla/5.0'})
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extract article content
                article_div = article_soup.find("div", class_='article-body-commercial-selector')
                temp_article = ''
                if article_div:
                    for p in article_div.find_all('p'):
                        text = p.get_text()
                        temp_article += "\n" + text

                if temp_article.strip():  # Check if the article text is available
                    print(headline_text)
                    print(f'https://www.theguardian.com/{headline_link}')
                    print("Article Text:", temp_article.strip())

                    # Extract article image
                    article_image = article_soup.find("meta", property="og:image")
                    if article_image:
                        print("Article Image:", article_image['content'])
                    else:
                        print("No article image found.")
                else:
                    print(f"No article text available for '{headline_text}'")
            else:
                print("No headline found or structure doesn't match the expected format.")

scrape()
