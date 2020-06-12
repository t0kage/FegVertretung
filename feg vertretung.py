from bs4 import BeautifulSoup #modul zur auslese der Internetseite importieren
import urllib3, smtplib, json #Modul zur verbindung mit der website importieren
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#mit der website verbinden
http = urllib3.PoolManager()
#einloggen
headers = urllib3.util.make_headers(basic_auth='feg:vertretung')
#funktion zur ermittlung der seitenanzahl von tag(b)
def seitenanzahl(b):
    for element in b.find_all("div"):
        seite = element.text
    seite = seite[-2]
    if seite == ' ':
        return(0)
    return(seite)

#generiert URL mit dem Tag und der Seite
def urlgen(tag,seite):
    tag = str(tag); seite = str(seite)
    if len(seite) >= 2: 
        seite = seite[0]
    stamm = 'http://anne-langner.de/feg-verwaltung.de/netzlaufwerk/VPlanWebsite/Monitor/Schueler_Tag'+ tag+ '/f1/subst_00'+ seite+ '.htm'
    stamm = str(stamm)
    response1 = http.request('GET', stamm, headers=headers)
    returnurl = BeautifulSoup(response1.data)
    return(returnurl)

#liest alle tabledatas der Url aus
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
N = {'email': 'nils.vgt@gmx.de', 'name': 'Nils', 'stufe': 'Q1', 'kurse': []}
M = {'email': 'mauricegoldmann@protonmail.com', 'name': 'Maurice', 'stufe': 'Q1', 'kurse': ['EKFG1', 'F5 L1', 'M L1', 'GEFG2', 'PH G8', 'D G2', 'E5 G3', 'PL G3', 'KU']}
J = {'email': 'nilsundjona@gmx.de', 'name': 'Jona', 'stufe': '07C', 'kurse': []}

def kecker(name, tag):
    stufe = name["stufe"]
    kurse = name["kurse"]

    vip = []

    for i in tag:
        if i[0] == stufe:
            vip.append(i)
    
    vip2 = []

    for i in vip:
        if i[2] in kurse:
            vip2.append(i)
    
    return(vip2)

def beautifultext(name, dielistehalt):  
    textmaster = []
    textmaster.append("Yo " + name['name'] + ', \n ')
    if len(dielistehalt) == 0:
            textmaster.append("Du hast heute nichts.")
    else:
        for i in dielistehalt:
            textmaster.append("Du hast heute " + i[6] + ' in der ' + i[1] +'. Stunde')
            if i[6] == 'EVA' or i[6] == 'Entfall':
                textmaster.append(".")
                pass
            else:
                textmaster.append(' in Raum ' + i[4] + ' bei ' + i[3] + ".")
                if i[7] == '\xa0':
                    pass
                else:
                    textmaster.append("  (" + i[7] + ") ")
            textmaster.append("\n")
    return("".join(textmaster))



#Email verschicken
def emailsend(adr, text = "bruh"):
    senderEmail = "vertretung_FEG@gmx.de"
    empfangsEmail = adr
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = empfangsEmail
    msg['Subject'] = "Dein Entfall/Vertretungs dings"

    emailText = text
    msg.attach(MIMEText(emailText, 'html'))

    server = smtplib.SMTP('mail.gmx.net', 587)
    server.starttls()
    server.login(senderEmail, "vertretung_FEG")
    text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail, text)
    server.quit()


emailsend(M['email'], beautifultext(M, kecker(M, all1)))
emailsend(N['email'], beautifultext(N, kecker(N, all1)))
emailsend(J['email'], beautifultext(J, kecker(J, all1)))