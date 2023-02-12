
import feedparser

class RSSHelper:
    
        
    def __init__(self) -> None:
        return

    def get_rss_titles(self, url) -> list[str]:
        url = feedparser.parse(url)
        return [entry.title for entry in url.entries]

    def get_rss_links(self, url) -> list[str]:
        url = feedparser.parse(url)
        return [entry.link for entry in url.entries]



