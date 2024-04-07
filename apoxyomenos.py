# Apoxyomenous - 'the scraper'
import requests
from bs4 import BeautifulSoup
import html5lib
import wikipediaapi

from src import helper

# version 1 - use bs4 to search given url
#   1.1 - autocomplete with confirmation in script









# version 2 - flesh this out with the wikipedia search

def main():
    """generate knowledge graph of mythology based on collected parameters scraped from text of each page"""


    return 


if __name__ == '__main__':
    # prompt user for url
    # wikiurl = input('input a url:\n')
    wikiurl = ''
    if len(wikiurl) == 0:
        wikiurl = 'https://en.wikipedia.org/wiki/List_of_mythologies'
    
    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "h7"]

    r = requests.get(url=wikiurl)#, headers=heading_tags)

    soup = BeautifulSoup(r.content, 'html5lib')

    kg = {}

    # page has h1 and h2 tags with links in them; i want to follow those links and create a knowledge graph of pages linked to by these pages to 6 degrees
    

    for heading in soup.find_all(heading_tags):
        # get text content of heading
        heading_text = heading.get_text().strip()
        print(heading_text)

        subsections = []
        sibling = heading.find_next_sibling() 
        while sibling and sibling.name not in ['h1']:#, 'h2', 'h3', 'h4', 'h5']:
            if "h" in sibling.name.strip():
                subsections.append()
        kg[heading_text] = subsections

    # print kg
    for heading, subsections in kg.items():
        print(f"{heading}")
        for subsection in subsections:
            print(f" - {subsection}")

    print('done!')