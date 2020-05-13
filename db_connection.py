# class for connecting to the database
import mysql.connector

host = 'localhost'
useradmin = 'sysadmin'
user = 'sysadmin'  #'dbuser'
passwd_admin = 'localhost'
passwd = 'localhost'
database = 'flashcards'

mydb = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

class Db_connection:
   # mycursor = mydb.cursor()
    
    def __init__(self):
        self = self

    def create_card_db(entry):
        mycursor = mydb.cursor()
        sqlform = "Insert into cards(mainsubject, catagory, question, answer, additional_info) values(%s,%s,%s,%s,%s)"
        cards = [entry[0], entry[1], entry[2], entry[3],entry[4]]
        mycursor.execute(sqlform,cards)
        mydb.commit()


    def del_card_db(cardID):
        mycursor = mydb.cursor()
        sql = "DELETE FROM cards WHERE CardId = %s"
        id = (cardID,)
        mycursor.execute(sql,id)
        mydb.commit()
        print(mycursor.rowcount, "record deleted")

    def update_card_db(self, column, entry):
        pass

    def display_card_db(cardID):
        pass
        mycursor = mydb.cursor()
        sql = ("Select * from cards WHERE CardId = %s")
        id = (cardID,)
        mycursor.execute(sql, id)
        display_card = mycursor.fetchone()
        for row in display_card:
            return display_card

    def retrieve_cards_db(self, group):
        pass