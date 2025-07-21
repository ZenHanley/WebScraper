from bs4 import BeautifulSoup
import requests

# Send a GET request to the specified URL
response = requests.get("https://quotes.toscrape.com")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the desired data from the soup object
quotes = soup.find_all("span", attrs={"class":"text"})

for quote in quotes:
    print(quote.text)
