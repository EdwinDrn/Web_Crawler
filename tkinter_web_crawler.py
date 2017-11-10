import requests
from bs4 import BeautifulSoup

import Tkinter
from Tkinter import *


root = Tk()
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.s2ki.com/" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        #This is the source code from the website
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a'):
            href = link.get('href')
            print href
        page += 1

button1 = Button(root, text = "Web Parse", command = trade_spider)
button1.bind("<Button-1>")
button1.pack()

button2 = Button(root, text = "This does not work")
button2.bind("<Button-1>")
button2.pack()

root.mainloop()
trade_spider()
