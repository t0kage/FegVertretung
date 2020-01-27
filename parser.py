from bs4 import BeautifulSoup
import urllib3

#connecting to website
http = urllib3.PoolManager()
url1 = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag1/f1/subst_001.htm'
url2 = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag2/f1/subst_001.htm'
#logs in
headers = urllib3.util.make_headers(basic_auth='feg:vertretung')
response1 = http.request('GET', url1, headers=headers)
response2 = http.request('GET', url2, headers=headers)
tag1 = BeautifulSoup(response1.data)
tag2 = BeautifulSoup(response2.data)
#soup = inhalt (anscheinend)

tag = tag2 #veränderbar

#definiert Funktion zum auslesen der Daten in eine Liste aus Acht Listen
def ausleser(url):


    rows = []

    i = 0
    z = 0

    columns = []

    for element in url.find_all("td"):
        i += 1
        if i >= 3 and z < 8:
            columns.append(element.text)
            #print(columns[z])
            z += 1
            if z == 8:
                rows.append(columns[:])
                columns[:] = []
                z = 0
    return(rows)


print(ausleser(tag)[0][0])

klasse = input('Klasse(05A):')

for l in range(12):
    if klasse in str(ausleser(tag)[l][0]):
        print(ausleser(tag)[l])

