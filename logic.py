from db import get_connection

def get_price(product, country, user_type):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT price FROM pricing
        WHERE product=? AND country=? AND user_type=?
    """, (product, country, user_type))

    result = cur.fetchone()
    conn.close()

    return result[0] if result else "Not found"


def get_sla(user_type):
    return {
        "individual": "98.5%",
        "business": "99.5%",
        "enterprise": "99.9%"
    }.get(user_type, "Unknown")


def apply_discount(price, enterprise=False, annual=False):
    if enterprise:
        price *= 0.7
    if annual:
        price *= 0.85
    return round(price, 2)