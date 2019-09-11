import connection, data_manager
from random import randint


number_of_dg_cards = 14
number_of_tr_cards = 33

@connection.connection_handler
def get_starting_dg_cards(cursor):
    cursor.execute("""
                    SELECT * FROM dungeon_cards;
                   """)
    all_cards = cursor.fetchall()

    cards_at_start = 4
    cards_in_hands = []
    random_numbers = []

    for i in range(0, cards_at_start):
        while True:
            random = randint(0, number_of_dg_cards-1)
            if random == 7:
                random == randint(0, number_of_dg_cards-1)
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

    cards_at_start = 4
    cards_in_hands = []
    random_numbers = []

    for i in range(0, cards_at_start):
        while True:
            random = randint(0, number_of_tr_cards-1)
            if random not in random_numbers:
                random_numbers.append(random)
                break
        cards_in_hands.append(all_cards[random])

    return cards_in_hands

@connection.connection_handler
def draw_dg_card(cursor):
    random_id = data_manager.random_dg_card()

    cursor.execute("""
        SELECT * FROM dungeon_cards 
        WHERE id = %(random_id)s;
    """, {'random_id': random_id})

    return cursor.fetchall()


@connection.connection_handler
def draw_tr_card(cursor):
    random_id = data_manager.random_tr_card()

    cursor.execute("""
        SELECT * FROM treasure_cards 
        WHERE id = %(random_id)s;
    """, {'random_id': random_id})

    return cursor.fetchall()

@connection.connection_handler
def get_all_dg_cards(cursor):
    cursor.execute("""
        SELECT * FROM dungeon_cards;
    """)

    return cursor.fetchall()


@connection.connection_handler
def get_all_tr_cards(cursor):
    cursor.execute("""
        SELECT * FROM treasure_cards;
    """)

    return cursor.fetchall()

