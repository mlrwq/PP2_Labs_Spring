from connect import get_connection

target = input("Введите имя или номер для удаления: ")

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (target, target))
        conn.commit()
        print("❌ Удаление выполнено.")
