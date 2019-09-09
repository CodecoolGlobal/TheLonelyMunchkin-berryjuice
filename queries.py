import connection


@connection.connection_handler
def get_monsters(cursor):
    cursor.execute("""
                    SELECT * FROM dungeon_cards 
                    ORDER BY id;
                   """)
    monsters = cursor.fetchall()

    return monsters
