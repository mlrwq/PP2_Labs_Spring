from connect import get_connection

name = input("enter name ")
phone = input("enter number ")

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO phonebook2 (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Added!")
