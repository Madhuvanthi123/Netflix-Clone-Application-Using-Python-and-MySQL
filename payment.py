from db import get_connection

def make_payment(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    amount = 199

    print("\n💳 PAYMENT SECTION")
    print("1. Subscription Plan - ₹199")

    choice = input("Enter 1 to proceed or 0 to cancel: ")

    if choice == "1":
        confirm = input(f"Confirm payment of ₹{amount}? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute(
                "INSERT INTO payments (user_id, amount, status) VALUES (%s, %s, %s)",
                (user_id, amount, "PAID")
            )
            conn.commit()
            print("✅ Payment successful!")
        else:
            print("❌ Payment cancelled!")
    else:
        print("❌ Payment cancelled!")

    conn.close()

def check_payment(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM payments WHERE user_id=%s AND status='PAID'",
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()
    return result
