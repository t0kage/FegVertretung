#dieser script funktioniert mit der seite.
#es leitet die formulardateien von ui.html zu einer json datei oder so
import json
import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
grade = form.getvalue('grade')
kurse = form.getvalue('kurse')

print(kurse)

#person_dict = {"name":"maurice", "age":"16"}

#with open("db.txt","w") as json_file:
    #json.dump(person_dict, json_file)