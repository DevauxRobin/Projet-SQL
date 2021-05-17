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


def display_table(table, title ="", start = 0, end = None):
### Affiche une table.


def display(text, title = "Requête table"):
### Affiche le résultat de la requête.
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()

table = []
for i in range(3,10):
    add_request(table,"req",i,".txt")

display_table(table,"title",0,7)