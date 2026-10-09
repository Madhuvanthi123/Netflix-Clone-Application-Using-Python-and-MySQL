from register import register, login
from payment import make_payment, check_payment
from watchlist import view_watchlist, add_to_watchlist
from ratings import rate_movie, view_my_ratings, view_all_ratings
from reports import generate_report, view_reports, init_file
import sys

def main_menu(user_id):
    while True:
        print("\n" + "="*40)
        print("🎬 NETFLIX CLONE - MAIN MENU")
        print("="*40)
        print("1. 📺 View Watchlist")
        print("2. ➕ Add to Watchlist")
        print("3. ⭐ Rate a Movie")
        print("4. 📊 View My Ratings")
        print("5. 🌟 View All Movies Ratings")
        print("6. 💳 Make Payment (₹199)")
        print("7. 📄 Generate Report")
        print("8. 📁 View Reports")
        print("9. 🚪 Logout")
        print("="*40)
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == "1":
            view_watchlist(user_id)
        elif choice == "2":
            add_to_watchlist(user_id)
        elif choice == "3":
            rate_movie(user_id)
        elif choice == "4":
            view_my_ratings(user_id)
        elif choice == "5":
            view_all_ratings()
        elif choice == "6":
            payment_status = check_payment(user_id)
            if payment_status:
                print("✅ Payment already done!")
            else:
                make_payment(user_id)
        elif choice == "7":
            generate_report(user_id)
        elif choice == "8":
            view_reports()
        elif choice == "9":
            print("👋 Logging out... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

def main():
    init_file()
    
    while True:
        print("\n" + "="*40)
        print("🎬 WELCOME TO NETFLIX CLONE")
        print("="*40)
        print("1. 🔐 Login")
        print("2. 📝 Register")
        print("3. 🚪 Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            user = login()
            if user:
                user_id = user[0]
                main_menu(user_id)
        elif choice == "2":
            register()
        elif choice == "3":
            print("👋 Thank you for using Netflix Clone!")
            sys.exit()
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()