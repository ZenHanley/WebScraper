from bs4 import BeautifulSoup
import requests

# Send a GET request to the specified URL
response = requests.get("https://learngerman.dw.com/en/nicos-weg/c-36519797")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the desired data from the soup object
titles = soup.findAll("h3", attrs={"class":"t1duk5k2"})

for title in titles:
    print(titles.text)