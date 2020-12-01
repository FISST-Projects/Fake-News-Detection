import requests
import csv
from csv import writer
from csv import reader
from bs4 import BeautifulSoup
import urllib.request as ureq
import json


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
    website = ureq.urlopen(theurl).read()
    # Parse the html of the site with soup
    soup = BeautifulSoup(website, 'lxml')
    # Get all the headers
    headers = soup.find_all('h2', {'class':'post-title'})
    # Extract title text from each header
    titles = list(map(lambda h: h.text.strip(), headers))
    # Extract link from each header
    links = list(map(lambda h: h.find('a')['href'], headers))
    create_rows(titles, links, rows)

def create_rows(Titles, Links, rows):
    arr = []
    for i in range(len(Links)):
        arr.append(Titles[i])
        arr.append(Links[i])
        arr.append('No conclusion')
        arr.append('FactChecker')
        rows.append(arr)
        arr = []

def add_columns(filename):

    # with open(filename) as input, open('demo005.csv', 'w') as output:
    #     non_blank = (line for line in input if line.strip())
    #     output.writelines(non_blank)

    label = 'No conclusion'
    source = 'FactChecker'
    # Open the input_file in read mode and output_file in write mode
    with open(filename, 'r', encoding = 'utf-8') as read_obj, \
            open('FactCheckDataset.csv', 'w',encoding = 'utf-8' ) as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append the default text in the row / list
            row.pop(2)
            row.append(label)
            row.append(source)
            # Add the updated row / list to the output file
            csv_writer.writerow(row)

def main():
    filename = "demo005.csv"
    # fields = ['Title', 'Link', 'Label', 'Source']
    # # data rows of csv file
    # rows = []
    # pages = range(1, 38)
    # for i in pages:
    #     url = 'https://www.factchecker.in/fact-check/2' + str(i) + '/'
    #     get_titles_and_links(url, rows)
    #
    # write_to_csv(fields, rows, filename)
    add_columns(filename)

if __name__ == "__main__":
    main()
