# Applied Databases Project
# Author: Philip Cullen
# Conference Management Application
#
# Technologies Used:
# - Python
# - MySQL
# - Neo4j
#
# This application allows users to:
# - View conference sessions and speakers
# - Manage attendees
# - View and create attendee connections
# - View conference room information

# Import Neo4j database functions
from neo4j_db import (
    test_neo4j_connection,
    get_connected_attendees,
    add_connection,
    connection_exists,
    get_total_connections
)

# Import MySQL database functions
from mysql_db import (
    test_mysql_connection,
    search_speakers_sessions,
    get_attendees_by_company,
    get_company_name,
    attendee_exists,
    add_attendee,
    get_attendee_name,
    get_rooms,
    get_conference_summary,
    get_shared_session_attendees
)

# Cache room data so newly added rooms are not shown
# until the application is restarted
cached_rooms = None


# Display speakers, sessions, and room information
def view_speakers_sessions():
    search_text = input("\nEnter speaker name or part of name: ")

    # Search for matching speakers
    results = search_speakers_sessions(search_text)

    # Display message if no speakers found
    if len(results) == 0:
        print("\nNo speakers found.")
    else:
        print("\nSpeakers & Sessions")
        print("-" * 50)

        # Display speaker details
        for speaker_name, session_title, room_name in results:
            print(f"Speaker: {speaker_name}")
            print(f"Session: {session_title}")
            print(f"Room: {room_name}")
            print("-" * 50)


# Display attendees for a selected company
def view_attendees_by_company():
    while True:
        company_id = input("\nEnter company ID or 'x' to return to menu: ")

        # Return to main menu
        if company_id.lower() == "x":
            return

        # Validate numeric company ID
        if not company_id.isdigit():
            print("Invalid input. Please enter a numeric company ID.")
            continue

        # Check if company exists
        company = get_company_name(company_id)

        if company is None:
            print("Company ID does not exist. Please try again.")
            continue

        # Retrieve attendee information
        results = get_attendees_by_company(company_id)

        # Check if company has attendees registered
        if len(results) == 0:
            print("Company exists, but has no attendees registered for any sessions. Please try again.")
            continue

        break

    company_name = company[0]

    print(f"\nCompany: {company_name}")
    print("-" * 60)

    # Display attendee information
    for _, attendee_name, dob, session_title, speaker_name, room_name in results:
        print(f"Attendee: {attendee_name}")
        print(f"Date of Birth: {dob}")
        print(f"Session: {session_title}")
        print(f"Speaker: {speaker_name}")
        print(f"Room: {room_name}")
        print("-" * 60)


# Add a new attendee to the MySQL database
def add_new_attendee():
    print("\nAdd New Attendee")

    # Get attendee details from user
    attendee_id = input("Enter attendee ID: ")
    name = input("Enter attendee name: ")
    dob = input("Enter date of birth YYYY-MM-DD: ")
    gender = input("Enter gender Male/Female: ")
    company_id = input("Enter attendee company ID: ")

    # Check if attendee ID already exists
    if attendee_exists(attendee_id):
        print(f"***ERROR*** Attendee ID: {attendee_id} already exists")
        return

    # Validate gender input
    if gender not in ["Male", "Female"]:
        print("***ERROR*** Gender must be Male/Female")
        return

    # Check if company exists
    company = get_company_name(company_id)

    if company is None:
        print(f"***ERROR*** Company ID: {company_id} does not exist")
        return

    # Attempt to add attendee to database
    try:
        add_attendee(attendee_id, name, dob, gender, company_id)
        print("Attendee successfully added")

    # Display database error messages
    except Exception as e:
        print(f"***ERROR*** {e}")


# Display attendees connected to a selected attendee
def view_connected_attendees():
    while True:
        attendee_id = input("\nEnter Attendee ID or 'x' to return to menu: ")

        # Return to main menu
        if attendee_id.lower() == "x":
            return

        # Validate attendee ID
        if not attendee_id.isdigit():
            print("***ERROR*** Invalid Attendee ID")
            continue

        # Check if attendee exists in MySQL
        attendee = get_attendee_name(attendee_id)

        if attendee is None:
            print("***ERROR*** Attendee does not exist")
            continue

        break

    attendee_name = attendee[0]

    print(f"Attendee Name: {attendee_name}")

    # Retrieve Neo4j connections
    connected_ids = get_connected_attendees(attendee_id)

    # Display no connections message
    if len(connected_ids) == 0:
        print("\nNo connections")
        return

    print("\nThese Attendees are connected:")

    # Display connected attendees
    for connected_id in connected_ids:
        connected_name = get_attendee_name(connected_id)

        if connected_name is not None:
            print(f"{connected_id} | {connected_name[0]}")


# Create a new attendee connection in Neo4j
def add_attendee_connection():
    print("\nAdd Attendee Connection")

    while True:

        # Get first attendee ID
        attendee_id_1 = input("Attendee ID 1 or 'x' to return to menu: ")

        if attendee_id_1.lower() == "x":
            return

        # Get second attendee ID
        attendee_id_2 = input("Attendee ID 2 or 'x' to return to menu: ")

        if attendee_id_2.lower() == "x":
            return

        # Validate numeric IDs
        if not attendee_id_1.isdigit() or not attendee_id_2.isdigit():
            print("***ERROR*** Both Attendee IDs must be numbers.")
            continue

        # Prevent self-connections
        if attendee_id_1 == attendee_id_2:
            print("***ERROR*** An Attendee cannot connect to him/herself")
            continue

        # Check if attendees exist in MySQL
        attendee_1 = get_attendee_name(attendee_id_1)
        attendee_2 = get_attendee_name(attendee_id_2)

        if attendee_1 is None or attendee_2 is None:
            print("***ERROR*** One or both attendee IDs do not exist.")
            continue

        # Prevent duplicate connections
        if connection_exists(attendee_id_1, attendee_id_2):
            print("***ERROR*** These attendees are already connected.")
            continue

        # Create Neo4j relationship
        add_connection(attendee_id_1, attendee_id_2)

        print(f"Attendee {attendee_id_1} is now connected to Attendee {attendee_id_2}")
        break


# Display cached room information
def view_rooms():
    global cached_rooms

    # Load rooms from database only once
    if cached_rooms is None:
        cached_rooms = get_rooms()

    print("\nRoom ID | Room Name | Capacity")

    # Display room details
    for room_id, room_name, capacity in cached_rooms:
        print(f"{room_id} | {room_name} | {capacity}")


# Main application menu
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
        print("7 - View Conference Summary")
        print("8 - Recommend Connections")
        print("x - Exit Application")

        # Get user menu choice
        choice = input("Choice: ").lower()

        # Execute selected menu option
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

        elif choice == "7":
            view_conference_summary()

        elif choice == "8":
            recommend_connections()

        elif choice == "x":
            print("\nExiting application...")
            break

        else:
            print("\nInvalid choice. Please try again.")

# Display conference summary statistics
def view_conference_summary():

    summary = get_conference_summary()
    total_connections = get_total_connections()

    print("\nConference Summary")
    print("-" * 40)

    print(f"Total Attendees: {summary['attendees']}")
    print(f"Total Companies: {summary['companies']}")
    print(f"Total Sessions: {summary['sessions']}")
    print(f"Total Rooms: {summary['rooms']}")
    print(f"Total Neo4j Connections: {total_connections}")

# Recommend attendees based on shared sessions
def recommend_connections():

    attendee_id = input("\nEnter Attendee ID: ")

    if not attendee_id.isdigit():
        print("***ERROR*** Invalid Attendee ID")
        return

    attendee = get_attendee_name(attendee_id)

    if attendee is None:
        print("***ERROR*** Attendee does not exist")
        return

    recommendations = get_shared_session_attendees(attendee_id)

    filtered_recommendations = []

    # Remove attendees already connected in Neo4j
    for recommended_id, recommended_name in recommendations:

        if not connection_exists(attendee_id, recommended_id):
            filtered_recommendations.append(
                (recommended_id, recommended_name)
            )

    if len(filtered_recommendations) == 0:
        print("\nNo recommendations available")
        return

    print("\nRecommended Connections")
    print("-" * 40)

    for recommended_id, recommended_name in filtered_recommendations:
        print(f"{recommended_id} | {recommended_name}")

# Main application entry point
def main():

    # Test MySQL connection
    if test_mysql_connection():
        print("MySQL server connected ✔")

    else:
        print("MySQL connection failed ❌")
        return

    # Test Neo4j connection
    if test_neo4j_connection():
        print("Neo4j connected ✔")

    else:
        print("Neo4j connection failed ❌")
        return

    # Start application menu
    main_menu()


# Run the application
if __name__ == "__main__":
    main()