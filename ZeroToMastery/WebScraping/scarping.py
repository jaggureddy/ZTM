import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
subtext = soup.select('.subtext')


def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key=lambda k: k['Points'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'Points': points})
    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hacker_news(links, subtext))
