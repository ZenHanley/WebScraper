from bs4 import BeautifulSoup
import requests

# Define the URL to scrape
url = "https://learngerman.dw.com/en/nicos-weg/c-36519797"

# Send a GET request to the URL
page = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Extract the desired data from the soup object
titles = soup.find_all("h3", attrs={"class":"t1duk5k2"})

for title in titles:
    print(title.text)
