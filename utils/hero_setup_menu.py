import os

from .get_name import get_name

def hero_setup_menu() -> None:
    os.system('clear')
    from classes.heros import Warrior, Wizard, Cleric, Thief
    name = get_name()
    action = input('Choose your hero\'s trade:\n\n(1) Warrior\n(2) Wizard\n(3) Cleric\n(4) Thief\n\n(Q) Quit:\n\n')
    hero_classes = {
        '1': Warrior,
        '2': Wizard,
        '3': Cleric,
        '4': Thief
    }
    hero = None

    if action in hero_classes:
        hero_class = hero_classes[action]
        hero = hero_class(name=name)
        hero.name = name
    elif action == 'Q':
        quit()
    else:
        print('Invalid action. Please try again.')

    print(f'You are {hero.name} the {hero.__class__.__name__}!')

    return hero