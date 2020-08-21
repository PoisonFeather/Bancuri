from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
from random import randrange
import time

url = 'https://www.rotalianul.com/colectie-de-bancuri-pentru-toate-gusturile/'
data=requests.get(url)


soup = BeautifulSoup(data.text,'html.parser')
while True:
    banc = soup.find_all('p')[randrange(len(soup.find_all('p')))].get_text()
    print(banc)
    toaster=ToastNotifier()
    toaster.show_toast(title="haha", msg=banc, duration=15)
    print(len(banc))
    time.sleep(10)
