#!"C:\Winpython\python-3.8.5.amd64\python.exe"
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="123456789", db="monde")
cursor=conn.cursor()
cursor.execute("show tables")
rows = cursor.fetchall()
def debuthtml():
    print("Content-type: text/html")
    print("\n")
    print("<html><head>")
    print("\n")
    print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
    print("</head><body>")

def finhtml():
    print("</body></html>")
debuthtml()  
table = "<table>\n"     
for row in rows:
    table += "<tr><td>\n"+str(row[0])+"</td></tr>\n"
table +="</table>\n"
print(table)
finhtml()