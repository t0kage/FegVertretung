# FegVertretung
Wir versuchen die Daten des vertretungsplans unserer Schule auszulesen und jeden der sich eingetragen hat bei Vertretung oder Entfall per Email zu Benachrichtigen.
# Herangehensweise
Der Plan ist es eine Website zu haben auf der man seine Email-Adresse und Fächer angibt. Diese werden dann in einer Json Datei gespeichert. Als nächstes kommt das Pythonprogramm zum parsen des Vertretungsplans ins Spiel, dieses erstellt eine Liste mit allen Vertretungsfällen und gleicht diese mit den Daten aus der Json Datei ab und schickt dann die Emails raus.
