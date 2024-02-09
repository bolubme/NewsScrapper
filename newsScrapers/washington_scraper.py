import requests
from bs4 import BeautifulSoup
from urlFile import washingtonUrl


def scrape():
    for url in washingtonUrl:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for article in soup.find_all('a', class_='flex hover-blue'):
            headline_text = article.find('h3',
                                         class_='font-md font-bold font--headline lh-sm gray-darkest hover-blue mb-0 antialiased mb-xxs').text
            headline_link = article.get('href')
            print('------------------------------------------')
            print(headline_text)
            print(headline_link)

            article_response = requests.get(headline_link, headers={'User-Agent': 'Mozilla/5.0'})
            article_soup = BeautifulSoup(article_response.text, 'html.parser')

            # Extracting article text
            temp_article = ""
            for div in article_soup.find_all("div", class_="article-body"):
                for p in div.find_all("p"):
                    text = p.get_text()
                    if "Sign up to get the rest free" in text:
                        continue
                    temp_article += "\n" + text

            print("Article Text:")
            print(temp_article)

            # Extracting images
            image_container = article_soup.find('div', id='lede-art-fig')
            if image_container:
                img = image_container.find('img')
                if img:
                    srcset_attribute = img.get('srcset')
                    if srcset_attribute:
                        # Splitting srcset attribute into individual URLs
                        srcset_urls = srcset_attribute.split(',')

                        # Selecting one URL (e.g., the first one)
                        selected_url = srcset_urls[0].split()[0]
                        print("Selected Image URL:", selected_url)

            print('------------------------------------------')


