from urllib.request import urlopen


switcher={
0:'http://pythonscraping.com/pages/page1.html',
1:'http://pythonscraping.com/pages/page1.html',
2:'http://pythonscraping.com/pages/page1.html',
3:'http://pythonscraping.com/pages/page1.html',
4:'http://pythonscraping.com/pages/page1.html',
5:'http://pythonscraping.com/pages/page1.html',
6:'http://pythonscraping.com/pages/page1.html'
}

selection = input("Enter number: ")
print('\n\t' + switcher.get(int(selection)) + '\n')
result = switcher.get(int(selection), -1)
html = urlopen(result)
print(html.read())
