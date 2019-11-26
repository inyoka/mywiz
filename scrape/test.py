#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

switcher={
0:'http://pythonscraping.com/pages/page1.html',
1:'http://www.chandrakumala.com',
2:'http://www.ipacindo.com',
3:'http://pythonscraping.com/pages/page1.html',
4:'http://pythonscraping.com/pages/page1.html',
5:'http://pythonscraping.com/pages/page1.html',
6:'http://pythonscraping.com/pages/page1.html'
}

selection = int(input("Enter number: "))
print('\n\t' + switcher.get(selection) + '\n')

result = switcher.get(selection, -1)


try:
    html = urlopen(result)
    if html is None:
        print('URL not found')

except HTTPError as e :
    print(e)
 

page = html.read()
print(page)

soup = BeautifulSoup(page, "html.parser")
print('\n')
print(soup.h1)
