from html_finder import HTMLFinder
from xpath_finder import XpathFinder
from request import make_request

import json


URL = 'https://www.olx.pl/sport-hobby/rowery/rowery-gorskie/q-marlin-7/'


def main():
    html_response = make_request(URL)

    finder = HTMLFinder(('div', 'offer-wrapper'))
    finder.feed(str(html_response))
    finder.save_data()

    xpath = XpathFinder()
    zmienna = xpath.find_by_xpath("//a/strong/text()")
    zmienna2 = xpath.find_by_xpath("//p[@class='price']/strong/text()")
    zmienna3 = xpath.find_by_xpath("///i[@data-icon='location-filled']/following-sibling::text()")
    list = []
    
    for offer in finder.get_data():
        dict = {}
        dict['title'] = next(zmienna)
        dict['price'] = next(zmienna2).replace(' ', '').replace('zł', '')
        dict['location'] = next(zmienna3)
        list.append(dict)
     
    
    with open('output/result.json', 'w', encoding='utf8') as file:
        json.dump(list, file, ensure_ascii=False)

    prices = [int(dict['price']) for dict in list if 'price' in dict]
    print(round(sum(prices) / len(list)))
    


if __name__ == "__main__":
    main()







