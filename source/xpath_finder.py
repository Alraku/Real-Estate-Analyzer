from io import StringIO
from lxml import html


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


    def find_by_xpath(self, xpath):
        for i in self.tree.xpath(xpath):
            yield i


# XP = XpathFinder()
# for i in XP.find_by_xpath("//p[@class='price']/strong/text()"):
#     print(i)
