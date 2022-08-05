from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from source.globals import HEADERS


def make_request(URL: str) -> str:
    try:
        request = Request(URL, headers=HEADERS)
        response = urlopen(request)
        return decode_utf8(response)

    except (HTTPError, URLError) as error:
        print(error.status, error.reason)


def decode_utf8(response: str) -> str:
    return response.read().decode("utf-8")