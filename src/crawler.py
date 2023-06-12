import requests
from bs4 import BeautifulSoup

# the website is of the form "https://cwe.mitre.org/data/definitions/XXX.html"
# where XXX is the weakness ID


# get the html of given CWE ID
def get_html_soup(CWE_ID):
    web_prefix = "https://cwe.mitre.org/data/definitions/"
    url = web_prefix + str(CWE_ID) + ".html"
    headers = {
	    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Aoyou/LWZ7QlJdJ2VcKDotKjxgLHZryjo9WGUUOQbkaNCCSrcYs0Rm9cAk1fGdZQ=="
	}
    resp = requests.get(url, headers = headers)
    if resp.status_code == 200:
        return BeautifulSoup(resp.text,"lxml")
    else:
        FileNotFoundError

# parse the type
def parse_type(soup):
    try:
        weakness_type = soup.find('div', id = 'CWEDefinition').find('div', class_ = 'title').tr.find_all('span',style="font-weight:normal")
        return [x.string for x in weakness_type]
    except:
        return "No Type"

# parse the name
def parse_name(soup):
    try:
        name_with_colon = soup.find('h2', style="display:inline; margin:0px 0px 2px 0px; vertical-align: text-bottom").string
        name = name_with_colon.split(":",1)[1]
        return name
    except:
        return 'No Name'

# parse the description
def parse_desc(soup):
    try:
        desc = soup.find('div', id = 'Description').find('div', class_ = 'detail').div.string
        return desc
    except:
        return "No desc"

def parse_phase(soup):
    try:
        phases = soup.find('div', id = 'Modes_Of_Introduction').find('div', class_ = "tabledetail").find_all('td', valign="middle")
        return [phase.string for phase in phases[::2]]
    except:
        return "No phase"

def has_c_code_example(soup):
    try:
        example_sections = soup.find('div', id = 'Demonstrative_Examples').find('div', class_ = 'detail').find_all('div', id = 'ExampleCode')
        for example in example_sections:
            if "</span>C" in str(example):
                return "Yes"
        return "No"
    except:
        return "ExNo"

