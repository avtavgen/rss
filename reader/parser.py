from datetime import datetime

import feedparser

from reader.models import RssFeed

URL_LENTA = "https://lenta.ru/rss/news"
URL_MEDUZA = "https://meduza.io/rss/all"

URL_LIST = [URL_LENTA, URL_MEDUZA]


def parse():
    for url in URL_LIST:
        d = feedparser.parse(url)
        for entrie in d.entries:
            rf = RssFeed()
            rf.name = url
            rf.title = entrie.title
            rf.link = entrie.link
            rf.description = entrie.summary
            rf.date = entrie.published
            try:
                rf.img_url=entrie.links[1]['href']
                rf.get_remote_image()
            except:
                rf.save()
