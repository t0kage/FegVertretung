from bs4 import BeautifulSoup
import urllib3


#connecting to website
http = urllib3.PoolManager()
#logs in
headers = urllib3.util.make_headers(basic_auth='feg:vertretung')
#funktion zur ermittlung der seitenanzahltag1
def seitenanzahl(b):
    for element in b.find_all("div"):
        seite = element.text
    seite = seite[-2]
    if seite == ' ':
        return(0)
    return(seite)

def urlgen(tag,seite):
    tag = str(tag); seite = str(seite)
    if len(seite) >= 2: 
        seite = seite[0]
    stamm = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag'+ tag+ '/f1/subst_00'+ seite+ '.htm'
    stamm = str(stamm)
    response1 = http.request('GET', stamm, headers=headers)
    returnurl = BeautifulSoup(response1.data)
    return(returnurl)

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


url = urlgen(1,1)

smax = seitenanzahl(url)
#liste mit allem
all1 = []
all2 = []
def zusammenfuegen(bigmama,tag):
        for i in range(1,int(smax)+1):
            url = urlgen(tag,i)
            bigmama.extend(ausleser(url))
        return(bigmama)

all1, all2 = zusammenfuegen(all1, 1), zusammenfuegen(all2, 2)

#okaaay 1.Teil finished!!!  all1 = Tag1, all2 = Tag2
#Der nächste Teil sollte in der DB checken, welche Leute frei haben
