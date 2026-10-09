from db import get_connection

def view_watchlist(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT m.title 
        FROM watchlist w
        JOIN movies m ON w.movie_id = m.id
        WHERE w.user_id = %s
    """, (user_id,))

    data = cursor.fetchall()

    print("\n📋 --- Your Watchlist ---")
    if data:
        for i, d in enumerate(data, 1):
            print(f"{i}. {d[0]}")
    else:
        print("No movies in watchlist")

    conn.close()

def add_to_watchlist(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title FROM movies")
    movies = cursor.fetchall()
    
    print("\n🎬 Available Movies:")
    for movie in movies:
        print(f"{movie[0]}. {movie[1]}")
    
    try:
        movie_id = int(input("\nEnter Movie ID to add to watchlist: "))
        cursor.execute(
            "INSERT INTO watchlist (user_id, movie_id) VALUES (%s, %s)",
            (user_id, movie_id)
        )
        conn.commit()
        print("✅ Added to watchlist!")
    except:
        print("❌ Invalid Movie ID or already in watchlist!")
    finally:
        conn.close()