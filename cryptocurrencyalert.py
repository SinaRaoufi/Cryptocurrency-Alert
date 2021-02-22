import requests
from bs4 import BeautifulSoup

URL = 'https://coin360.com/'

# crpto information
symbol = 'BTC'
lowerThan = '56,500.00'
greaterThan = '56,500.00'

isDone = False
while(isDone == False):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    rows = soup.find_all('tr')
    rows.remove(rows[0])  # remove table header
    for row in rows:
        result = row.find_all('td')
        if(result[0].text.strip() == symbol):
            # check the condition
            if(result[3].text.strip() > greaterThan):
                print(result[3].text.strip())
                isDone = True
        # index 0 --> symbol
        # index 1 --> name
        # index 2 --> market cap
        # index 3 --> price
        # index 4 --> volume 24h
        # index 5 --> circulating cupply
        # index 6 --> change 24h
