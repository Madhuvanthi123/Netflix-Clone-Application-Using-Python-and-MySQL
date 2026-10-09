from db import get_connection
import csv
import os

def init_file():
    if not os.path.exists("reports.csv"):
        with open("reports.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["UserID", "Movie", "Rating", "Payment Status"])

def generate_report(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT u.id, m.title, r.rating, p.status
        FROM users u
        LEFT JOIN watchlist w ON u.id = w.user_id
        LEFT JOIN movies m ON w.movie_id = m.id
        LEFT JOIN ratings r ON u.id = r.user_id AND m.id = r.movie_id
        LEFT JOIN payments p ON u.id = p.user_id
        WHERE u.id=%s
    """, (user_id,))

    data = cursor.fetchall()
    conn.close()

    with open("reports.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("📄 Report saved to reports.csv")

def view_reports():
    if not os.path.exists("reports.csv"):
        print("No reports found")
        return

    with open("reports.csv", "r") as file:
        print("\n📊 --- REPORTS ---")
        reader = csv.reader(file)
        for row in reader:
            print(f"UserID: {row[0]}, Movie: {row[1]}, Rating: {row[2]}, Payment: {row[3]}")