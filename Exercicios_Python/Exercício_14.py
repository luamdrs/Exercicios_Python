import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('https://www.instagram.com/sciencebydata_/')
except urllib.error.URLError:
    print('O site não está acessível no momento!')
else:
    print('Consegui acessar o site com sucesso!')