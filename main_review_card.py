# main app to review flash cards
from cards import Cards

def game_on():
    pass
    select = input('Select option: ((A)dd card, (U)pdate card, (S)elect Subject, (L)ist Subjects, (Q)uit:  ')
    if select.lower() == 'a':
        add_card = Cards()
        add_card.create_card()
    elif select.lower() == 'u':
        update_card = Cards()
        update_card.edit_card()
    elif select.lower() == 's':
        study_time()
    elif select.lower() == 'l':
        list_cards = Cards()
        list_cards.display_cards()
    elif select.lower() == 'q':
        quit()
    else:
        print('Not a valid response, please try again')
        game_on()

def launch_app():
    print('Time to review some FlashCards,')
    start = input('Are you ready? Y/N')
    if start.lower() == 'y':
        game_on()
    elif start.lower() == 'n':
        print('goodbye')
        exit()
    else:
        print('Not a valid entry')
        launch_app()

def study_time():
    pass
    

launch_app()