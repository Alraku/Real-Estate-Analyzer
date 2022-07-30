import json

from lxml import html
from io import StringIO


file_path = "output/output.html"

class XpathFinder():

    def __init__(self) -> None:
        # Try opening the filename
        with open(file_path, 'r') as file:
            source_html = file.readlines()
            source_html = "".join(source_html)

        # Define an HTML parser object
        # Create a logical XML tree from the contents of parser_04
        HTML_parser = html.HTMLParser()
        self.tree = html.parse(StringIO(source_html), HTML_parser)


    def find_by_xpath(self, values_to_find) -> None:
        output_list = list()
        for key, value in values_to_find.items():
            xpath_finder = self.tree.xpath(value)
            for index, item in enumerate(xpath_finder):
                if index >= len(output_list):
                    output_list.append({
                            key: xpath_finder[index]
                            })
                else:
                    output_list[index].update({
                            key: xpath_finder[index]
                        })

        self.save_to_json(output_list)


    def next_page(self, xpath) -> bool:
        if len(self.tree.xpath(xpath)) == 0: 
            return False
        else: return True


    @classmethod
    def save_to_json(cls, output_list) -> None:
        with open('output/result.json', 'w', encoding='utf8') as file:
            json.dump(output_list, file, ensure_ascii=False)


XP = XpathFinder()
print(XP.next_page('//spaxd'))
