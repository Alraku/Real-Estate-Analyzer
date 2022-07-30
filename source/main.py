from request import make_request
from html_finder import HTMLFinder
from xpath_finder import XpathFinder


URL = 'https://www.olx.pl/sport-hobby/rowery/rowery-gorskie/q-marlin-7/'

def main():

    finder = HTMLFinder(('div', 'offer-wrapper'))
    finder.feed(make_request(URL))
    finder.save_data()

    values_to_find = {
        'title': "//a/strong/text()",
        'price': "//p[@class='price']/strong/text()",
        'location': "///i[@data-icon='location-filled']/following-sibling::text()"
    }

    XpathFinder().find_by_xpath(values_to_find)

    next_page = XpathFinder.next_page({'//some/xpath.mark'})
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)
    

if __name__ == "__main__":
    main()







