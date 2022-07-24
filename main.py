from typing import Tuple
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser


pstring = source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""


class WebHTMLParser(HTMLParser):

    def __init__(self, tag_to_find: Tuple[str, str, str]):
        super().__init__()
        self.reset()
        self.tag_to_find = tag_to_find
        self.NEWTAGS = ['one']
        self.NEWATTRS = []
        self.HTMLDATA = []

        # trzeba bedzie to jakos zaimplementowac tak jak scrapy, albo beatufiul soup dziala
        # czyli dajesz mu nazwe diva ktory powtarza sie (np jakas lista)
        # i on przeszukuje wsrod tych wszystkich divów ktore wystepuja dane tagi z klasami.

    def handle_starttag(self, tag, attrs):
        if tag == self.tag_to_find[0] and self.tag_to_find[1] in [(key) for key, value in attrs] and self.tag_to_find[2] in [(value) for key, value in attrs]:
            print(self.tag_to_find)
            
        dicted_attrs = dict(attrs)
        self.NEWTAGS.append(tag)
        if 'data-cy' in dicted_attrs:
            if "listing-ad-title" in dicted_attrs['data-cy']:
                if tag == 'a' and attrs[0][0] == 'href':
                    print(attrs[0][1])
                    self.HTMLDATA.append
        self.NEWATTRS.append(attrs)

    def handle_data(self, data):
        data = " ".join(data.split())
        if self.NEWTAGS[-1] == 'strong' and self.NEWTAGS[-2] == 'a':
            if data != '':
                self.HTMLDATA.append(data)
            
    def clean(self):
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []

    def print(self):
        print(*self.HTMLDATA, sep='\n')






url = 'https://www.olx.pl/sport-hobby/rowery/rowery-gorskie/q-marlin-7/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Content-Type': 'text/html; charset=utf-8'}

try:
    req = Request(url, headers= headers)
    response = urlopen(req)
    html = response.read().decode("utf-8")
    parserxd = WebHTMLParser(('div', 'class', 'offer-wrapper'))
    parserxd.feed(str(html))
    #parserxd.print()


except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)




