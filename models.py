from config import get_db_connection

def get_faqs(domain):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT question, answer FROM faqs WHERE domain = %s", (domain,))
    faqs = cursor.fetchall()
    conn.close()
    return faqs

def add_faq(question, answer, domain):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO faqs (question, answer, domain) VALUES (%s, %s, %s)", (question, answer, domain))
    conn.commit()
    conn.close()

def get_domains():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT domain FROM faqs")
    domains = [row["domain"] for row in cursor.fetchall()]
    conn.close()
    return domains
