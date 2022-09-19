from request import make_request
from html_filter import HTMLFilter
from xpath_finder import XpathFinder


def scrap_data():

    URL = 'https://www.olx.pl/sport-hobby/rowery/rowery-gorskie/q-marlin-5/'

    finder = HTMLFilter(('div', 'offer-wrapper'))
    finder.feed(make_request(URL))
    finder.save_data()

    values_to_find = {
        'title': "//a/strong/text()",
        'price': "//p[@class='price']/strong/text()",
        'location': "///i[@data-icon='location-filled']/following-sibling::text()"
    }

    test_var = XpathFinder().xpath(values_to_find).get()
    # print(type(test_var), test_var)


    # next_page = XpathFinder().xpath({'next_page_button': '//h6[@class="css-v3vynn-Text eu5v0x0"]/text()'}).get()
    # print(next_page)
    # if next_page is not None:
    #     pass
        #TODO Sprawić tal, aby nowa instancja XPATHFINDER nie korzystała z htmla przefiltrowanego tylko bazowego.
        #TODO Sprawić aby mozna było konkretne atrybuty (np. href) pobierać i wypisywać.
        # next_page = response.urljoin(next_page)
        # yield scrapy.Request(next_page, callback=self.parse)
    

if __name__ == "__main__":
    scrap_data()







