from bs4 import BeautifulSoup
# import lxml # for other websites 
import requests
from pprint import pprint

response = requests.get(url="https://news.ycombinator.com/news")

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

submissions = soup.find_all(class_ = "athing submission")
articles = soup.find_all(class_ = "titleline")

data = {}
index = 1

for submission, article in zip(submissions, articles):
    upvotes = soup.find(name = "span", id = f"score_{submission.get('id')}", class_ = "score")
    data[index] = {
            "id": submission.get("id"),
            "title": article.find("a").getText(),
            "link": article.find("a").get("href"),
            "upvotes": int(upvotes.text.split()[0]) if upvotes else "N/A"
            }
    index += 1

pprint(data)

'''
all_titles = soup.find_all("span", {'class': 'titleline'})
article_title = [title.find("a").getText() for title in all_titles]
article_links = [title.find("a").get("href") for title in all_titles]
article_upvotes = [score.text for score in soup.find_all("span", class_ = "score")]

print(len(article_title))
print(len(article_links))
print(len(article_upvotes))
'''