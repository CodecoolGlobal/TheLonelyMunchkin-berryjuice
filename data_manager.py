from random import randint


def get_gender_randomly():
    genders = ['male', 'female']
    random = randint(0, 1)

    return genders[random]


def random_dg_card():
    number_of_dg_cards = 15
    while True:
        random_id = randint(0, number_of_dg_cards - 1)
        if random_id == 7:
            random_id = randint(0, number_of_dg_cards - 1)
        else:
            break

    return random_id

def random_tr_card():
    number_of_dg_cards = 33
    random_id = randint(0, number_of_dg_cards - 1)

    return random_id
