import requests 
from bs4 import BeautifulSoup 


def bitcoin():
    link = 'https://www.calc.ru/Bitcoin-k-dollaru-online.html'
    r = requests.get(link).text

    soup = BeautifulSoup(r, 'lxml')
    block = soup.find('div', {'class': 't18'})
    btc_to_usd = block.find_all('b')[1].text
    print('1 BTC =', btc_to_usd)


def usd():
    link = 'https://www.calc.ru/kurs-USD-RUB.html'
    responce = requests.get(link).text

    soup = BeautifulSoup(responce, 'lxml')
    block1 = soup.find('div', {'class' : 't18'}).text
    usd_to_rub = block1[29:34]
    print('1 USD =', usd_to_rub, 'RUB')


def eur():
    link = 'https://www.calc.ru/forex-EUR-RUB.html'
    res = requests.get(link).text
 
    soup = BeautifulSoup(res, 'lxml')
    blo = soup.find('div', {'class': 't18'})
    eur = blo.find_all('b')[1].text
    print('1 EUR =',eur)

if __name__ == '__main__':
    bitcoin()
    eur()
    usd()