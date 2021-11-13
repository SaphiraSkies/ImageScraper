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

    # parsed_url = urlparse(url)
    # base_url = parsed_url.scheme + "://" + parsed_url.netloc

    data = "data"

    # This stores the list of image URLS
    image_list = []

    # Get all images
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    # Add each image to the list
    for image in images:
        first_four = image['src'][0:4]          # This is used for removing erroneous results
        if first_four != data:
            # print(base_url + image['src'])
            # print(image['src'])
            image_list.append(image['src'])

    return image_list