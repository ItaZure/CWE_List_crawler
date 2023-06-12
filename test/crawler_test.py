import sys
sys.path.insert(0, sys.path[0]+"/../")
# from src import crawler
from src import crawler
import requests


soup = crawler.get_html_soup(415)
print(crawler.parse_type(soup))
print(crawler.parse_name(soup))
print(crawler.parse_desc(soup))
print(crawler.parse_phase(soup))
print(crawler.has_c_code_example(soup))
