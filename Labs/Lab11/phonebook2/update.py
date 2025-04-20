from connect import get_connection

field = input("what do you want to change? (name/phone): ").strip().lower()
target = input("enter name or phone: ")
new_value = input("new value: ")

with get_connection() as conn:
    with conn.cursor() as cur:
        if field == 'name':
            cur.execute("UPDATE phonebook2 SET name = %s WHERE phone = %s", (new_value, target))
        elif field == 'phone':
            cur.execute("UPDATE phonebook2 SET phone = %s WHERE name = %s", (new_value, target))
        conn.commit()
        print("Updated")
