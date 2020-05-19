# will contain all methods releatd to the flash cards, including the creation, compiling, and ???
import db_connection 
from db_connection import Db_connection
import random

class Cards:

    def __init__(self):
        self = self

    def create_card(self):
        entry = []
        print("Create flashcard: ")
        subject = input('Please enter main subject: ')
        category = input('Please enter catagory: ')
        question = input('Plese enter the flashcard Question: ')
        answer = input('Please enter the Answer: ')
        add_info = input('Please add any additional info: ')
        entry = (subject, category, question, answer, add_info)
        create_card_entry = Db_connection()
        create_card_entry.create_card_db(entry)

    def delete_card(self):
        delete_id = int(input('Please enter the ID # for the card you would like deleted: ' ))
        delete_card_details = Db_connection()
        delete_card_details.del_card_db(delete_id)

    
    def edit_card(self):
        edit_id = int(input('Please enter the ID for the card that you want to update: '))
        edit_card_details = Db_connection()
        result = edit_card_details.display_card_db(edit_id)
        print(f"1: Card ID: {result[0]}")
        print(f"2: Subject: {result[1]}")
        print(f"3: Question: {result[2]}")
        print(f"4: Answer: {result[3]}")
        print(f"5: Addional Info: {result[4]}")

    

    def display_cards(self):
        pass
        display_cards_db = Db_connection()
        return display_cards_db.retrieve_card_list_db()
        #print(list)


    def display_subject_list(self, column, cat=''):
        pass
        listing = []
        display_subject_db = Db_connection()
        if cat == '':
            trup_list = display_subject_db.display_subject_list_db(column)
        else:
            trup_list = display_subject_db.display_subject_list_db(column, cat)
        for t in trup_list:
            for i in t:
                listing.append(i)
        return listing




#testcard = Cards()
#testcard.edit_card()
#testcard.create_card()
#testcard.delete_card()
#testcard.edit_card()
#testcard.display_cards()
#testcard.display_subject_list()