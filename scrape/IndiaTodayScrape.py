import requests
import csv
from bs4 import BeautifulSoup
import urllib.request as ureq
from urllib.request import Request, urlopen
import json
import re

def write_to_csv(fields, rows, filename):

    with open(filename, 'w') as csvfile:
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
    Fact_Check = soup.find(class_= "view-content")
    # Get all the headers
    headers = Fact_Check.find_all('div', {'class':'detail'})
    # Extract title text from each header
    titles = list(map(lambda h: h.find('h2')['title'], headers))
    # Extract link from each header
    links = list(map(lambda h: h.find('a')['href'], headers))
    create_rows(titles, links, rows)

def create_rows(Titles, Links, rows):
    arr = []
    for i in range(len(Links)):
        arr.append(Titles[i])
        arr.append("https://www.indiatoday.in" + Links[i])
        get_labels_and_source(arr, "https://www.indiatoday.in" + Links[i])
        rows.append(arr)
        arr = []

def get_labels_and_source(arr, link):
    try:
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        website = urlopen(req).read()
        # Parse the html of the site with soup
        soup = BeautifulSoup(website, 'lxml')
        # Get all classes under Fact-Check section
        Fact_Check = soup.find(class_= "factcheck-result-img")
        images = Fact_Check.find_all('img', {'src':re.compile('.gif')})
        for image in images:
            if(image['src'] == "https://akm-img-a-in.tosshub.com/indiatoday/factcheck/1c.gif"):
                arr.append("Half True")
            elif(image['src'] == "https://akm-img-a-in.tosshub.com/indiatoday/factcheck/2c.gif"):
                arr.append("Mostly lies")
            elif(image['src'] == "https://akm-img-a-in.tosshub.com/indiatoday/factcheck/3c.gif"):
                arr.append("Absolutely lies")
            else:
                arr.append("No conclusion")
    except:
        arr.append("No conclusion")

    arr.append("India Today")

def main():
    filename = "India_Today_Dataset.csv"
    fields = ['Title', 'Link', 'Label', 'Source']
    # data rows of csv file
    rows = []
    for i in range(1,103):
        url = 'https://www.indiatoday.in/fact-check?page=' + str(i)
        get_titles_and_links(url, rows)

    write_to_csv(fields, rows, filename)

if __name__ == "__main__":
    main()
