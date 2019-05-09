import requests
import numpy as np
import time

#https://www.bitmarket.pl/json/BTCPLN/ticker.json
#https://coinroom.com/api/ticker/BTC/PLN
#https://bitbay.net/API/Public/BTCPLN/ticker.json

def fetch_data(url,name):
    response = requests.get(url)
    data = response.json()
    best_bid = data['bid']
    best_ask = data['ask']
    return [best_ask,best_bid,name]

def check_data(url1,name1,url2,name2):
    dane2 = []
    dane2.append(fetch_data(url1,name1))
    dane2.append(fetch_data(url2,name2))
    best_ask = 0
    best_bid = 100000000
    for i in dane2:
        if i[0] > best_ask:
            best_ask = i[0]
            ask_name = i[2]
        if i[1] < best_bid:
            best_bid = i[1]
            bid_name = i[2]
    print('Currently the', bid_name, 'exchange market is better for buying whilst', ask_name,
          'is better for selling\nBest bid:', best_bid, '\nBest ask:', best_ask)

def fetch_user(url):
    response = requests.get(url)
    data = response.json()
    id = data["results"][0]['id']['value']
    username = data["results"][0]['login']['username']
    first_name = data["results"][0]['name']['first']
    last_name = data["results"][0]['name']['last']
    return [id,username,first_name,last_name,100000,10] # ostatnie dwie: ilosc pln,ilosc btc

def wymiana_btc_pln(user1,user2):
    liczba_bitcoinow = np.random.uniform(0.001,2)
    bitcoin_to_pln_bid = liczba_bitcoinow * fetch_data('https://bitbay.net/API/Public/BTCPLN/ticker.json','bitbay.net')[1]
    bitcoin_to_pln_ask = liczba_bitcoinow * fetch_data('https://bitbay.net/API/Public/BTCPLN/ticker.json','bitbay.net')[0]
    if dane[user1][4] >= bitcoin_to_pln_bid and dane[user2][5] >= liczba_bitcoinow:
        dane[user1][4] = dane[user1][4] - bitcoin_to_pln_bid
        dane[user1][5] = dane[user1][5] + liczba_bitcoinow
        dane[user2][4] = dane[user2][4] + bitcoin_to_pln_ask
        dane[user2][5] = dane[user2][5] - liczba_bitcoinow
        print(dane[user1][1], "exchanged", round(liczba_bitcoinow,3), "BTC with", dane[user2][1], "for", round(bitcoin_to_pln_ask,3), "PLN")

check_data('https://bitbay.net/API/Public/BTCPLN/ticker.json','bitbay.net','https://www.bitmarket.pl/json/BTCPLN/ticker.json','bitmarket.pl')

dane = []
k = 100 # liczba ludzi
print("Trwa pobieranie bazy uzytkownikow...")
while len(dane) < k:
    try:
        dane.append(fetch_user('https://randomuser.me/api/?inc=id,name,login'))
    except:
        pass

begin = time.time()
for i in range(k):
    l1 = np.random.randint(0,k)
    l2 = np.random.randint(0,k)
    while l1 == l2:
        l2 = np.random.randint(0,k)
    wymiana_btc_pln(l1,l2)
    time.sleep(2/5)

end = time.time()
czass = end - begin
print(int(czass))

# BID - > kupno
# ASK - > sprzedaż

#TASKS (11p)

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)