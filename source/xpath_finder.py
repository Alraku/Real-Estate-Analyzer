import os, json

from lxml import html
from io import StringIO
from typing import Dict, List
from exceptions import EmptyFileError


class XpathFinder():

    def __init__(self) -> None:
        """
        # Try opening the filename
        # Define an HTML parser object
        # Create a logical XML tree from the contents of parser_04
        """
        self.found = list()
        self.file_path = "output/output.html"

        if is_file_empty(self.file_path):
            with open(self.file_path, 'r') as file:
                source_html = file.readlines()
                source_html = "".join(source_html)
        else: 
            raise EmptyFileError(self.file_path)

        HTML_parser = html.HTMLParser()
        self.tree = html.parse(StringIO(source_html), HTML_parser)


    def xpath(self, values_to_find):
        for key, value in values_to_find.items():
            xpath_finder = self.tree.xpath(value)
            for index, item in enumerate(xpath_finder):
                if index >= len(self.found):
                    self.found.append({
                            key: xpath_finder[index]})
                else:
                    self.found[index].update({
                            key: xpath_finder[index]})

        self.save_to_json(self.found)
        return self


    def next_page(self, xpath) -> bool:
        response = self.tree.xpath(xpath)
        if len(response) != 0:
            return True


    @classmethod
    def save_to_json(cls, output_list) -> None:
        with open('output/result.json', 'w', encoding='utf8') as file:
            json.dump(output_list, file, ensure_ascii=False)


    def get(self) -> Dict:
        """Returns only first found element from list."""
        return self.found[0] if len(self.found) > 0 else None


    def get_all(self) -> List[Dict]:
        """Returns whole list of found elements."""
        return self.found


def is_file_empty(fpath) -> bool: 
    if fpath is None: 
        raise TypeError('File path is of type None.')
    try:
        return os.path.getsize(fpath) > 0
    except FileNotFoundError as error:
        raise error
