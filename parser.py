from bs4 import BeautifulSoup
import urllib3

#connecting to website
http = urllib3.PoolManager()
url1 = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag1/f1/subst_001.htm'
url2 = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag1/f1/subst_001.htm'
#logs in
headers = urllib3.util.make_headers(basic_auth='feg:vertretung')
response1 = http.request('GET', url1, headers=headers)
response2 = http.request('GET', url2, headers=headers)
tag1 = BeautifulSoup(response1.data)
tag2 = BeautifulSoup(response2.data)
#soup = inhalt (anscheinend)

for element in tag1.find_all("tr"):
    print(element.text)
