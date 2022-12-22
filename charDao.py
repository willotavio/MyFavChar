import mysql.connector as mc
from tkinter import *

connection = mc.connect(
    host='localhost',
    user='root',
    password='',
    database='myfavchar',
)

# create
def create(charname, chargrade, chardesc):
    connection.connect()
    cursor = connection.cursor()
    command = f'INSERT INTO favoriteChar (nm_character, gd_character, ds_character) VALUES ("{charname}", {chargrade}, "{chardesc}")'
    cursor.execute(command)
    connection.commit()
    command = 'SELECT nm_character, gd_character, ds_character FROM favoriteChar'
    cursor.execute(command)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

# read
def read(listChar):
    connection.connect()
    cursor = connection.cursor()
    command = 'SELECT nm_character, gd_character, ds_character FROM favoriteChar'
    cursor.execute(command)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    listChar.delete(0, END)
    for i in result:
        listChar.insert(0, i)

# update
def update(charid, charname, chargrade, chardesc):
    connection.connect()
    cursor = connection.cursor()
    command = f'UPDATE favoriteChar SET nm_character = "{charname}", gd_character = {chargrade}, ds_character = "{chardesc}" WHERE cd_character = {charid}'
    cursor.execute(command)
    connection.commit()
    command = 'SELECT nm_character, gd_character, ds_character FROM favoriteChar'
    cursor.execute(command)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

# delete
def delete(charid):
    connection.connect()
    cursor = connection.cursor()
    command = f'DELETE FROM favoriteChar WHERE cd_character = {charid}'
    cursor.execute(command)
    connection.commit()
    command = 'SELECT nm_character, gd_character, ds_character FROM favoriteChar'
    cursor.execute(command)
    result = cursor.fetchall()
    cursor.close()
    connection.close()