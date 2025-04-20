from connect import get_connection

search = input("enter name or phone to search: ")

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM phonebook2
            WHERE name ILIKE %s OR phone LIKE %s
        """, (f'%{search}%', f'%{search}%'))

        rows = cur.fetchall()
        for row in rows:
            print(row)
