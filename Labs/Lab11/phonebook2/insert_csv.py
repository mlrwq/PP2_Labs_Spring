import csv
from connect import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        with open('contacts.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute("INSERT INTO phonebook2 (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("insert from csv completed")
