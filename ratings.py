from db import get_connection

def rate_movie(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title FROM movies")
    movies = cursor.fetchall()
    
    print("\n⭐ --- Rate Movies ---")
    for movie in movies:
        print(f"{movie[0]}. {movie[1]}")
    
    try:
        movie_id = int(input("\nEnter Movie ID to rate: "))
        rating = int(input("Enter Rating (1-5 stars): "))
        
        if 1 <= rating <= 5:
            cursor.execute(
                "SELECT * FROM ratings WHERE user_id=%s AND movie_id=%s",
                (user_id, movie_id)
            )
            existing = cursor.fetchone()
            
            if existing:
                cursor.execute(
                    "UPDATE ratings SET rating=%s WHERE user_id=%s AND movie_id=%s",
                    (rating, user_id, movie_id)
                )
                print("✅ Rating updated!")
            else:
                cursor.execute(
                    "INSERT INTO ratings (user_id, movie_id, rating) VALUES (%s, %s, %s)",
                    (user_id, movie_id, rating)
                )
                print("✅ Rating added!")
            
            conn.commit()
        else:
            print("❌ Rating must be between 1 and 5!")
    except:
        print("❌ Invalid input!")
    finally:
        conn.close()

def view_my_ratings(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT m.title, r.rating 
        FROM ratings r
        JOIN movies m ON r.movie_id = m.id
        WHERE r.user_id = %s
    """, (user_id,))
    
    ratings = cursor.fetchall()
    
    print("\n⭐ --- Your Ratings ---")
    if ratings:
        for movie, rating in ratings:
            stars = "⭐" * rating
            print(f"{movie}: {rating}/5 {stars}")
    else:
        print("You haven't rated any movies yet!")
    
    conn.close()

def view_all_ratings():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT m.title, AVG(r.rating) as avg_rating, COUNT(r.rating) as total_ratings
        FROM movies m
        LEFT JOIN ratings r ON m.id = r.movie_id
        GROUP BY m.id
        ORDER BY avg_rating DESC
    """)
    
    ratings = cursor.fetchall()
    
    print("\n⭐ --- All Movies Average Ratings ---")
    for movie, avg_rating, total in ratings:
        if avg_rating:
            print(f"{movie}: {avg_rating:.1f}/5 (from {total} ratings)")
        else:
            print(f"{movie}: No ratings yet")
    
    conn.close()