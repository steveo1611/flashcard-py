# classes for displaying the q and a: for entering the new questions and tracking what was given for the answers.
from cards import Cards
from db_connection import Db_connection
import random


class Display:

    def __init__(self):
        self = self

    def select_subject_category(self):
        pass
        # ask of what subject and catagory to compile cards for.
        study_card = Cards()
        subject_select = ''
        cat_select = ''
        subject_list = study_card.display_subject_list('mainsubject')
        print(subject_list)
        subject = input('Please select which Subject to review: ')
        if subject.lower() == 'q':
            print('Good Bye')
            return exit()
        for i in subject_list:
            if i != subject.lower():
                pass
            else:
                subject_select = i
                print(subject_select)

        cat_list = study_card.display_subject_list(subject_select, 'category')
        print(cat_list)
        category = input('Please select which category to review: ')
        if category.lower() == 'q':
            print('Good Bye')
            return exit()
        for i in cat_list:
            if i != category.lower():
                pass
            else:
                cat_select = i

        return (subject_select, cat_select)
# maybe next version will use the generation/interation

    def get_collection(self, cgrouping):
        collection = []
        card_collection = Db_connection()
        collection_order = card_collection.retrieve_subject_cards_db(cgrouping)
        random.shuffle(collection_order)
        return collection_order

