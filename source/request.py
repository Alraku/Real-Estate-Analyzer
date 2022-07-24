from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Content-Type': 'text/html; charset=utf-8'
    }


def make_request(url):
    try:
        request = Request(url, headers=HEADERS)
        response = urlopen(request)
        html_response = response.read().decode("utf-8")
        return html_response
        
    except HTTPError as e:
        print(e.status, e.reason)
    except URLError as e:
        print(e.reason)