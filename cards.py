# will contain all methods releatd to the flash cards, including the creation, compiling, and ???
import db_connection 
from db_connection import Db_connection

class Cards:

    def __init__(self):
        self = self

    def create_card(self):
        entry = []
        print("Create flashcard: ")
        subject = input('Please enter main subject: ')
        catagory = input('Please enter catagory: ')
        question = input('Plese enter the flashcard Question: ')
        answer = input('Please enter the Answer: ')
        add_info = input('Please add any additional info: ')

        entry = (subject, catagory, question, answer, add_info)
        Db_connection.create_card_db(entry)

    def delete_card(self):
        delete_id = int(input('Please enter the ID # for the card you would like deleted: ' ))
        Db_connection.del_card_db(delete_id)

    
    def edit_card(self):
        pass
        edit_id = int(input('Please enter the ID for the card that you want to update: '))
        edit_card_details = Db_connection.display_card_db(edit_id)
        print(edit_card_details)
    

    def display_cards(self):
        pass

#Cards().create_card()
#Cards().delete_card()
Cards().edit_card()    