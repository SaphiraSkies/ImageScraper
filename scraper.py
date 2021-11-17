###################################################################################
# Hannah Moon - Image Scraper Microservice - Scraper Function
# 11/11/2021
# This program contains functions for scraping image URLs from a static website.
###################################################################################

from bs4 import BeautifulSoup
import requests

# Formats a list as a JSON string
def LISTtoJSON(list):
    str_list = "["
    str_list = str_list + ', '.join(list)
    str_list = str_list + "]"
    return '{"URL":' + str_list + '}'

# Formats a JSON string to just the URL
def JSONtoURL(json):
    size = len(json)
    url = json[8:size-2]
    return url

# This function takes a given URL and scrapes all images under img tags.
# It returns a list of the image URLs.
def scrape_site(url):
    # This variable is used to help filter results
    data = "data"

    # This stores the list of image URLS
    image_list = []

    # Get all images
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    # Add each image to the list
    for image in images:
        first_four = image['src'][0:4]          # Remove some erroneous results
        if first_four != data:
            image_list.append(image['src'])

    return image_list