import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    data = []

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        data.append([text, author, ", ".join(tags)])

    return data


def main():
    url = 'http://quotes.toscrape.com'
    quotes_data = scrape_quotes(url)

    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Quote', 'Author', 'Tags'])
        writer.writerows(quotes_data)

    print("Data has been written to quotes.csv")


if __name__ == "__main__":
    main()
