import psycopg2
from config import load_config

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)

# опционально, тест соединения
if __name__ == '__main__':
    conn = get_connection()
    print("✅ Connected!")
    conn.close()
