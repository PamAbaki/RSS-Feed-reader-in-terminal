import pprint
from main import RSSHelper

url = input("Enter the URL of the RSS feed: ")
rsh = RSSHelper()
titles = rsh.get_rss_titles(url)
links = rsh.get_rss_links(url)
combined = [(title, link) for title, link in zip(titles, links)]
for title, link in combined:
    print("Title:")
    pprint.pprint(title)
    print("Link:")
    pprint.pprint(link)
    print()


