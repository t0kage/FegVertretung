from bs4 import BeautifulSoup
import urllib3

#connecting to website
http = urllib3.PoolManager()
url = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/index_schueler.htm'
#logs in
headers = urllib3.util.make_headers(basic_auth='feg:vertretung')
response = http.request('GET', url, headers=headers)
soup = BeautifulSoup(response.data)
#soup = inhalt (anscheinend)
print(soup)
