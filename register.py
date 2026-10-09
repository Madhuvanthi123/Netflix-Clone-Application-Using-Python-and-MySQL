from db import get_connection
import mysql.connector
import sys

def register():
    conn = get_connection()
    cursor = conn.cursor()

    u = input("Enter Username: ").strip()
    p = input("Enter Password: ").strip()
    
    # Validate input
    if not u or not p:
        print("❌ Username and password cannot be empty!")
        conn.close()
        return
    
    # Check if username exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (u,))
    if cursor.fetchone():
        print(f"❌ Username '{u}' already exists! Please choose a different username.")
        conn.close()
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (u, p))
        conn.commit()
        print("✅ Registered Successfully!")
        print("🔐 You can now login with your credentials.")
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    finally:
        conn.close()

def login():
    conn = get_connection()
    cursor = conn.cursor()

    u = input("Enter Username: ").strip()
    p = input("Enter Password: ").strip()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (u, p))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"✅ Login Success! Welcome back, {u}!")
        return user
    else:
        print("❌ Invalid Login! Please check your credentials or register first.")
        return None