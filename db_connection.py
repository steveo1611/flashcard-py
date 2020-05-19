# class for connecting to the database
# NOTE FOR LATER - how do I reduce the calls to the database, return objects and not have to query everytime
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

    def create_card_db(self, entry):
        mycursor = mydb.cursor()
        sqlform = "Insert into cards(mainsubject, category, question, answer, additional_info) values(%s,%s,%s,%s,%s)"
        cards = [entry[0], entry[1], entry[2], entry[3],entry[4]]
        mycursor.execute(sqlform,cards)
        mydb.commit()


    def del_card_db(self, cardID):
        mycursor = mydb.cursor()
        sql = "DELETE FROM cards WHERE CardId = %s"
        id = (cardID,)
        mycursor.execute(sql,id)
        mydb.commit()
        print(mycursor.rowcount, "record deleted")

    def update_card_db(self, column, entry):
        pass

    def display_card_db(self, cardID):
        mycursor = mydb.cursor()
        sql = ("Select * from cards WHERE CardId = %s")
        id = (cardID,)
        mycursor.execute(sql, id)
        display_card = mycursor.fetchone()
        for row in display_card:
            return display_card

    def retrieve_card_list_db(self):
        mycursor = mydb.cursor()
        sql = ("SELECT * from cards")
        mycursor.execute(sql)
        collection = mycursor.fetchall()
        for i in collection:
            print(i)

    #def retrieve_subject_cards_db(self, subject='aws', cat= '' ):
    def retrieve_subject_cards_db(self, group):    
        #subject = "aws"
        #cat = "s3"
        collect_list = []
        mycursor= mydb.cursor(buffered=True)
        #sql_rows = "SELECT COUNT(*) FROM cards WHERE mainsubject = %s"
        #sub_var = (subject,)
        #mycursor.execute(sql_rows, sub_var)
        #row_count = (mycursor.fetchone())
        #row_count_int = int('{}'.format(row_count[0]))
        #sql = ("SELECT * from cards WHERE mainsubject = %s and category LIKE %s")
        sql = ("SELECT * from cards WHERE mainsubject = %s and category = %s")
        #value = (subject, cat)
        value = (group[0], group[1])
        mycursor.execute(sql, value)
        #collection = mycursor.fetchmany(row_count_int)
        collection = mycursor.fetchall()
        return collection

    def display_subject_list_db(self, column, cat=''):
        if cat != '':
            sql_column = f'SELECT DISTINCT {cat} FROM cards WHERE mainsubject = "{column}"'
        else:    
            sql_column = f'SELECT DISTINCT {column} FROM cards'
        mycursor = mydb.cursor()
        mycursor.execute(sql_column)
        return mycursor.fetchall()

        

#testdb = Db_connection()
#testdb.retrieve_cards_db()            
#testdb.retrieve_subject_cards_db()
#testdb.display_subject_list_db('mainsubject')