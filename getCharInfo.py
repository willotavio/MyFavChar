from charDao import *

def addchar(listChar, charName, charGrade, charDesc):
    charname = charName.get()
    chargrade = charGrade.get()
    chardesc = charDesc.get()
    create(charname, chargrade, chardesc)
    read(listChar)


def readchar(listChar):
    read(listChar)

def updatechar(listChar, charId, charName, charGrade, charDesc):
    charid = charId.get()
    charname = charName.get()
    chargrade = charGrade.get()
    chardesc = charDesc.get()
    update(charid, charname, chargrade, chardesc)
    read(listChar)

def deletechar(listChar, charId):
    charid = charId.get()
    delete(charid)
    read(listChar)
