# ==========================================
#        MOVIE RECOMMENDATION SYSTEM
# ==========================================

movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "mood": "Curious",
        "rating": 8.7
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "mood": "Excited",
        "rating": 9.0
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "mood": "Excited",
        "rating": 8.4
    },
    {
        "title": "The Hangover",
        "genre": "Comedy",
        "mood": "Happy",
        "rating": 7.7
    },
    {
        "title": "3 Idiots",
        "genre": "Comedy",
        "mood": "Happy",
        "rating": 8.4
    },
    {
        "title": "The Notebook",
        "genre": "Romance",
        "mood": "Romantic",
        "rating": 7.8
    },
    {
        "title": "Titanic",
        "genre": "Romance",
        "mood": "Romantic",
        "rating": 7.9
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "mood": "Curious",
        "rating": 8.8
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama",
        "mood": "Emotional",
        "rating": 8.8
    },
    {
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "mood": "Emotional",
        "rating": 8.0
    }
]


# ==========================================
# DISPLAY ALL MOVIES
# ==========================================

def show_movies():

    print("\n========== ALL MOVIES ==========")

    for movie in movies:
        print("--------------------------------")
        print("Title :", movie["title"])
        print("Genre :", movie["genre"])
        print("Mood  :", movie["mood"])
        print("Rating:", movie["rating"])


# ==========================================
# GET MOVIE RECOMMENDATION
# ==========================================

def recommend_movie():

    print("\n========== GET RECOMMENDATION ==========")

    print("\nAvailable Genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Sci-Fi")
    print("4. Romance")
    print("5. Drama")

    genre_choice = input("\nChoose a genre: ")

    if genre_choice == "1":
        genre = "Action"

    elif genre_choice == "2":
        genre = "Comedy"

    elif genre_choice == "3":
        genre = "Sci-Fi"

    elif genre_choice == "4":
        genre = "Romance"

    elif genre_choice == "5":
        genre = "Drama"

    else:
        print("❌ Invalid genre choice.")
        return

    print("\nAvailable Moods:")
    print("1. Excited")
    print("2. Happy")
    print("3. Curious")
    print("4. Romantic")
    print("5. Emotional")

    mood_choice = input("\nChoose your mood: ")

    if mood_choice == "1":
        mood = "Excited"

    elif mood_choice == "2":
        mood = "Happy"

    elif mood_choice == "3":
        mood = "Curious"

    elif mood_choice == "4":
        mood = "Romantic"

    elif mood_choice == "5":
        mood = "Emotional"

    else:
        print("❌ Invalid mood choice.")
        return

    print("\n========== RECOMMENDATIONS ==========")

    found = False

    for movie in movies:

        if movie["genre"] == genre and movie["mood"] == mood:

            print("--------------------------------")
            print("🎬 Title :", movie["title"])
            print("🎭 Genre :", movie["genre"])
            print("😊 Mood  :", movie["mood"])
            print("⭐ Rating:", movie["rating"])

            found = True

    if found == False:
        print("No movie found for this combination.")


# ==========================================
# SEARCH FOR A MOVIE
# ==========================================

def search_movie():

    print("\n========== SEARCH MOVIE ==========")

    search = input("Enter movie name: ")

    found = False

    for movie in movies:

        if search.lower() in movie["title"].lower():

            print("\nMovie Found!")
            print("--------------------------------")
            print("🎬 Title :", movie["title"])
            print("🎭 Genre :", movie["genre"])
            print("😊 Mood  :", movie["mood"])
            print("⭐ Rating:", movie["rating"])

            found = True

    if found == False:
        print("\n❌ Movie not found.")


# ==========================================
# SHOW TOP RATED MOVIES
# ==========================================

def top_rated_movies():

    print("\n========== TOP RATED MOVIES ==========")

    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    for movie in sorted_movies[:5]:

        print("--------------------------------")
        print("🎬", movie["title"])
        print("⭐ Rating:", movie["rating"])


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("========================================")
        print("       🎬 MOVIE RECOMMENDATION SYSTEM")
        print("========================================")

        print("1. Get Recommendation")
        print("2. Search Movie")
        print("3. Show All Movies")
        print("4. Show Top Rated Movies")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            recommend_movie()

        elif choice == "2":

            search_movie()

        elif choice == "3":

            show_movies()

        elif choice == "4":

            top_rated_movies()

        elif choice == "5":

            print("\n🎬 Thank you for using Movie Recommendation System!")
            print("Goodbye! 👋")
            break

        else:

            print("\n❌ Invalid choice. Please try again.")


# ==========================================
# START PROGRAM
# ==========================================

main()