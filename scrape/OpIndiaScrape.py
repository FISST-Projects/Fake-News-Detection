import requests
import csv
from bs4 import BeautifulSoup
import urllib.request as ureq
from urllib.request import Request, urlopen
import json


def write_to_csv(fields, rows, filename):

    with open(filename, 'w', encoding = 'utf-8') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
    # writing the fields
        csvwriter.writerow(fields)
    # writing the data rows
        csvwriter.writerows(rows)


def get_titles_and_links(theurl, rows):
    # Fetch the website
    req = Request(theurl, headers={'User-Agent': 'Mozilla/5.0'})
    website = urlopen(req).read()
    # Parse the html of the site with soup
    soup = BeautifulSoup(website, 'lxml')
    # Get all classes under Fact-Check section
    Fact_Check = soup.find(class_= "td_block_inner tdb-block-inner td-fix-index")
    # Get all the headers
    headers = Fact_Check.find_all('h3', {'class':'entry-title td-module-title'})
    # Extract title text from each header
    titles = list(map(lambda h: h.find('a')['title'], headers))
    # Extract link from each header
    links = list(map(lambda h: h.find('a')['href'], headers))
    create_rows(titles, links, rows)

def create_rows(Titles, Links, rows):
    arr = []
    for i in range(len(Links)):
        arr.append(str(Titles[i]))
        arr.append(str(Links[i]))
        arr.append("No conclusion")
        arr.append('opIndia')
        rows.append(arr)
        arr = []


def main():
    filename = "Op_India_Dataset.csv"
    fields = ['Title', 'Link', 'Label', 'Source']
    # data rows of csv file
    rows = []
    pages = range(26, 97)
    for i in pages:
        url = 'https://www.opindia.com/category/fact-check/page/' + str(i) + '/'
        get_titles_and_links(url, rows)

    write_to_csv(fields, rows, filename)

if __name__ == "__main__":
    main()
