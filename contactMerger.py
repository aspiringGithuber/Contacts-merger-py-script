import sqlite3 #to remove dupes and possibly other operations on the main contact list
import vobject #for vcf files a common format for contacts


def vcfToDB(count): #add contact to db according to merge conditions
    with open(file) as file: # for every contact in the file add to data base if not a dupe
        for contact in file:
            if(not dupe()):
                addtoDB()
            count+=1
                
    return

def DBToVcf(): # for every contact in the database convert back to Vcf
    with open(DB) as dataBase:
        for contact in dataBase:
            addtoVCF()
    return

def dupe():
    for row in db:
        if row[1] == row[2]:
            return True
    return False

def addtoDB():
    return

def addtoVCF():
    return

def main():
    conn = sqlite3

if __name__ == "__main__":
    main()
