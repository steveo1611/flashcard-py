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
            pass
            #print(i)
            subject_select = i
            print(subject_select)
            #return subject_select
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
            pass
            print(i)
            cat_select = i
            print(cat_select)
            #return cat_select        
    
    study_time()
    # randomize cards and display first card's question...

    # user answers question / then card's answser is displayed, keep count of questions/answers
    # display next

launch_app()