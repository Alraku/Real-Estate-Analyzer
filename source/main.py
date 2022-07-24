from pprint import pprint
from html_finder import HTMLFinder
from xpath_finder import XpathFinder
from request import make_request

from pprint import pprint
import json

URL = 'https://www.olx.pl/sport-hobby/rowery/rowery-gorskie/q-marlin-7/'


def main():
    html_response = make_request(URL)

    finder = HTMLFinder(('div', 'offer-wrapper'))
    finder.feed(str(html_response))
    # finder.save_data()

    xpath = XpathFinder()
    table = finder.get_data()
    for offer in range(10):
        dict = {
            'title': next(xpath.find_by_xpath("//a/strong/text()")),
            'price': next(xpath.find_by_xpath("//p[@class='price']/strong/text()"))
        }
     
    with open('result.json', 'w') as file:
        json.dump(dict, file)


if __name__ == "__main__":
    main()







