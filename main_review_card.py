# main app to review flash cards
from cards import Cards
from display_interact import Display


def game_on():
    pass
    select = input(
        'Select option: ((A)dd card, (U)pdate card, (S)elect Subject, (L)ist Subjects, (Q)uit:  \n')
    if select.lower() == 'a':
        new_card()
    elif select.lower() == 'u':
        update_card()
    elif select.lower() == 's':
        study_time()
    elif select.lower() == 'l':
        list_subject()
    elif select.lower() == 'q':
        print('Thank you and good-bye')
        quit()
    else:
        print('Not a valid response, please try again')
        game_on()


def launch_app():
    print('Time to review some FlashCards!!!\n')
    start = input('Are you ready? Y/N ')
    if start.lower() == 'y':
        game_on()
    elif start.lower() == 'n':
        print('goodbye')
        exit()
    else:
        print('Not a valid entry')
        launch_app()

def new_card():
    work = True
    add_card = Cards()
    add_card.create_card()
    while work == True:
        add_another_card = input('Do you want to add another card? y/n ')
        if add_another_card.lower() == 'y':
            new_card()
        elif add_another_card.lower() == 'n':
            print('Done, back to selection list')
            work = False
            game_on()
        else:
            print('Not a valid entry')


def update_card():
    edit = True
    edit_cards = Cards()
    edit_cards.edit_card()
    while edit == True:
        update_another_card = input('Do you want to edit another card? y/n ')
        if update_another_card.lower() == 'y':
            update_card()
        elif update_another_card.lower() == 'n':
            print('Done, back to selection list')
            edit = False
            game_on()
        else:
            print('Not a valid entry')

def study_time():
    quest_num = 0
    quest = True
    # ask of what subject and catagory to compile cards for.
    display = Display()
    grouping = display.select_subject_category()
    # grab all the cards and randomize order. done in the display_interact file
    collection = display.get_collection(grouping)
    for i in collection:
        quest_num += 1
        print(f'{quest_num} of {len(collection)}')
        print(f"\nQuestion: {i[3]} ")
        input('Please Enter your answer: '  )
        print(f'\nAnswer: {i[4]}\n')
        print(f'Additional details: {i[5]}\n')
    while quest == True:
        review_cards = input('\nDo you want to review more cards? y/n \n')
        if review_cards.lower() == 'y':
            study_time()
        elif review_cards.lower() == 'n':
            print('\nDone, back to selection list')
            quest = False
            game_on()
        else:
            print('Not a valid entry')
        
def list_subject():
    list = True
    list_cards = Cards()
    list_cards.display_cards()
    while list == True:
            list_cards_again = input('\nDo you want to list cards again? y/n ')
            if list_cards_again.lower() == 'y':
                list_subject()
            elif list_cards_again.lower() == 'n':
                print('\nDone, back to selection list')
                list = False
                game_on()
            else:
                print('Not a valid entry')


launch_app()
