import connection


@connection.connection_handler
def get_dg_cards(cursor):
    cursor.execute("""
                    SELECT * FROM dungeon_cards 
                    ORDER BY id;
                   """)
    cards = cursor.fetchall()

    return cards

@connection.connection_handler
def get_tr_cards(cursor):
    cursor.execute("""
                    SELECT * FROM treasure_cards 
                    ORDER BY id;
                   """)
    cards = cursor.fetchall()

    return cards