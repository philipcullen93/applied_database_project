from mysql_db import test_mysql_connection
from neo4j_db import test_neo4j_connection


from mysql_db import test_mysql_connection, search_speakers_sessions

def view_speakers_sessions():
    search_text = input("\nEnter speaker name or part of name: ")

    results = search_speakers_sessions(search_text)

    if len(results) == 0:
        print("\nNo speakers found.")
    else:
        print("\nSpeakers & Sessions")
        print("-" * 50)

        for speaker_name, session_title, room_name in results:
            print(f"Speaker: {speaker_name}")
            print(f"Session: {session_title}")
            print(f"Room: {room_name}")
            print("-" * 50)


def view_attendees_by_company():
    print("\nView Attendees by Company selected")


def add_new_attendee():
    print("\nAdd New Attendee selected")


def view_connected_attendees():
    print("\nView Connected Attendees selected")


def add_attendee_connection():
    print("\nAdd Attendee Connection selected")


def view_rooms():
    print("\nView Rooms selected")


def main_menu():
    while True:
        print("\nConference Management")
        print("\nMenu")
        print("1 - View Speakers & Sessions")
        print("2 - View Attendees by Company")
        print("3 - Add New Attendee")
        print("4 - View Connected Attendees")
        print("5 - Add Attendee Connection")
        print("6 - View Rooms")
        print("x - Exit Application")

        choice = input("Choice: ").lower()

        if choice == "1":
            view_speakers_sessions()
        elif choice == "2":
            view_attendees_by_company()
        elif choice == "3":
            add_new_attendee()
        elif choice == "4":
            view_connected_attendees()
        elif choice == "5":
            add_attendee_connection()
        elif choice == "6":
            view_rooms()
        elif choice == "x":
            print("\nExiting application...")
            break
        else:
            print("\nInvalid choice. Please try again.")


def main():
    if test_mysql_connection():
        print("MySQL server connected ✔")
    else:
        print("MySQL connection failed ❌")
        return

    if test_neo4j_connection():
        print("Neo4j connected ✔")
    else:
        print("Neo4j connection failed ❌")
        return

    main_menu()


if __name__ == "__main__":
    main()