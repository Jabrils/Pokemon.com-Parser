import urllib3 as u3
import urllib.request as ur

http = u3.PoolManager()

def GrabHTML(url):
    page = http.request('GET', url)
    return page.data.decode('utf-8')

def GrabHTML0(url):
    page = ur.urlopen(url)
    return page.read().decode('utf-8')