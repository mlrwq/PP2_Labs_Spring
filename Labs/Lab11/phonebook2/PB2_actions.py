from connect import get_connection

def search_by_pattern(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
            return cur.fetchall()
        
def upsert(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_user(%s, %s)", (name, phone))
            conn.commit()

def del_by_name_phone(text):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL del_by_name_phone(%s)", (text,))
            conn.commit()