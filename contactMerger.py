import sqlite3 #to remove dupes and possibly other operations on the main contact list
import vobject #for vcf files a common format for contacts


#function to convert .vcf(virtual contact file) to sql database

def vcfToDB(count, cursor, vcf): #add contact to db according to merge conditions
    try:
        with open(vcf, 'r', encoding="utf-8") as file: # for every contact in the file add to data base if not a dupe # not sure why encoding has to be that way causes error if not. fix purposed by claude
            for contact in vobject.readComponents(file.read()): #taken from google search
                if(not dupe(cursor, contact)):
                    addtoDB(count, cursor, contact)
                    count+=1
                else:
                    updateDB(cursor,contact) # todo(done) add sql query that updates numbers and emails for contacts
    except FileNotFoundError:
        print("invalid file")
    except Exception as e:
        print(f"unknown err{e}")
        
        
                
    return


#Todo
def DBToVcf(): # for every contact in the database convert back to Vcf # todo
    with open(DB) as dataBase:
        for contact in dataBase:
            addtoVCF()
    return

#helper for vcftodb decides if contact already exists which means no new entry and will update and existing entry instead
def dupe(cursor, contact): # current issue edge case where to people with same name can exist not handled
    cursor.execute('SELECT * from people')
    rows = cursor.fetchall()
    for row in rows:
        if row[1].lower() == contact.fn.value.lower():
            return True
    return False


#adds new contact to DB
def addtoDB(count, cursor, contact):
    nums = ""
    emails = ""
    if hasattr(contact, 'tel_list'): 
        for num in contact.tel_list:
            nums += num.value + ' '
    if hasattr(contact, 'email_list'):
        for email in contact.email_list:
            emails += email.value + ' '
    #use sql insert credits to geeksforgeeks
    cursor.execute('INSERT INTO people VALUES (?, ?, ?, ?)', (count, contact.fn.value, nums, emails))
    
    return

#updates existing contact in DB
def updateDB(cursor, contact):
    nums = ""
    emails = ""
    if hasattr(contact, 'tel_list'): 
        for num in contact.tel_list:
            nums += num.value + ' ' 
    if hasattr(contact, 'email_list'):
         for email in contact.email_list:
            emails += email.value + ' '
    cursor.execute('UPDATE people SET number = CONCAT(number, ?) WHERE name = ?', (nums,contact.fn.value))
    cursor.execute('UPDATE people SET email = CONCAT(email, ?) WHERE name = ?', (emails,contact.fn.value))

#ToDo
def addtoVCF():
    return

def main():
    count = 0 # counter var acts as ID
    vcf = input("enter vcf filename ")
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, number TEXT, email TEXT)') # make table if it doesnt exist
    print("Database and table created successfully.")
    
    vcfToDB(count, cursor, vcf)
    
    conn.commit() # save changes to db (though script was broken turns out i wasnt committing)
    
    

if __name__ == "__main__":
    main()
