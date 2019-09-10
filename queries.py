import connection
from random import randint

cards_at_start = 4


@connection.connection_handler
def get_starting_dg_cards(cursor):
    cursor.execute("""
                    SELECT * FROM dungeon_cards;
                   """)
    all_cards = cursor.fetchall()

    number_of_cards = len(all_cards)
    cards_in_hands = []
    random_numbers = []

    for i in range(0, cards_at_start):
        while True:
            random = randint(0, number_of_cards-1)
            if random not in random_numbers:
                random_numbers.append(random)
                break
        cards_in_hands.append(all_cards[random])

    return cards_in_hands

@connection.connection_handler
def get_starting_tr_cards(cursor):
    cursor.execute("""
                    SELECT * FROM treasure_cards;
                   """)
    all_cards = cursor.fetchall()

    number_of_cards = len(all_cards)
    cards_in_hands = []
    random_numbers = []

    for i in range(0, cards_at_start):
        while True:
            random = randint(0, number_of_cards-1)
            if random not in random_numbers:
                random_numbers.append(random)
                break
        cards_in_hands.append(all_cards[random])

    return cards_in_hands