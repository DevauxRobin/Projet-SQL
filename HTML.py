#!"C:\winpython\python-3.8.5.amd64\python.exe"
import tkinter
import os
import sqlite3


def create_connexion(db_file):
### Créer une connexion à la base de données SQLite du db_file.
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except error as e:
        print(e)
    return conn

conn = database_connexion("data/imdb.db")


def read_request(file):
### Apporte une requête puis et l'ajoute dans une liste vide.
    assert type(file) == str
    List = []
    with open(fichier,"r") as request:
        lines = filin.readlines()
        for line in lines:
            List.append(line)
    return List


def add_request(dico,file):
### Ajoute une requête dans un dictionnaire sous forme de liste.
    assert type(dico) == dict
    dico.append(read_request(file))
    return dico


def start_html():
### Début du code HTML
    print("Content-type: text/html")
    print("\n")
    print("<html><head>")
    print("\n")
    print(" <style> table, th, td {border: 1px solid black;  padding: 5px; border-collapse: collapse;} </style> ")
    print("</head><body>")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    start_html()
    table = "<table>\n"
    for row in rows:
        table += "<tr><td>\n"+str(row[0])+"</td></tr>\n"
    table +="</table>\n"
    print(table)
    finhtml()


request = read_request(Requêtes.txt)
execute_sql(conn,request)