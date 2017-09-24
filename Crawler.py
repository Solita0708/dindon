import requests
import urllib.request
import re
from bs4 import BeautifulSoup
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
soup = BeautifulSoup(opener.open('https://dinbendon.net/do'), "html5lib")

z = re.match(r".+>(?P<D1>\d{1,2}).+(?P<D2>\d{1,2}).+", str(soup.findAll('td', style="width: 6em;")[0]) )
g = int(z.group(1)) + int(z.group(2))

postdata = urllib.parse.urlencode({
    'signInPanel_signInForm:hf:0':'',
    'rememberMeRow:rememberMe':'on',
    'username':'@@@',
    'password':'@@@',
    'result':g,
    'submit':'µn¤J'
        }).encode("utf-8")

loginUrl = 'https://dinbendon.net/do/?wicket:interface=:1:signInPanel:signInForm::IFormSubmitListener'
result = BeautifulSoup(opener.open(loginUrl, postdata), "html5lib")

cookie.save(ignore_discard=True, ignore_expires=True)






table = result.find_all('table')[3]
td1 = table.find_all('td')[0:-1]
for i in td1:
    span1 = i.find_all('span')
    for j in span1:
        print (j.text)