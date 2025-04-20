from connect import get_connection

target = input("enter name or phone to delete: ")

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook2 WHERE name = %s OR phone = %s", (target, target))
        conn.commit()
        print("deleted.")
