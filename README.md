# Applied Databases Project - Conference Management Application

## Student
Philip Cullen

## Project Overview
This is a Python conference management application utilising both MySQL and Neo4j.

The application allows users to:
- View speakers, sessions, and rooms
- View attendees by company
- Add new attendees
- View attendee connections from Neo4j
- Add new attendee connections
- View room details
- View conference summary statistics
- Recommend possible attendee connections

## Technologies Used
- Python
- MySQL
- Neo4j
- mysql-connector-python
- neo4j Python driver

## Required Databases

### MySQL
Import appdbproj.sql into MySQL.

This creates the database:
appdbproj

### Neo4j
Create a Neo4j instance and run the provided Neo4j setup script, appdbprojNeo4j.json.

The graph contains Attendee nodes and CONNECTED_TO relationships.

## Python Packages
1. Install the required packages with: 

   pip install -r requirements.txt

3. If installing manually:

   pip install mysql-connector-python neo4j

## Running the Application
1. Ensure MySQL is running.

   - Note: If MySQL Server is not connected navigate to Services -> MySQL80 and Start the Service

3. Ensure Neo4j is running.

4. Enter python app.py in the terminal

   - Note: The application will confirm that both the MySQL and Neo4j databases are connected.

### Main Menu
Once the script is working correectly the following should be displayed in the terminal:

Conference Management

Main Menu

1 - View Speakers and Sessions
2 - View Attendees by Company
3 - Add New Attendees
4 - View Connected Attendees
5 - Add Attendee Connection
6 - View Rooms
7 - View Conference Summary
8 - Recommend Connections
x - Exit Application

### New Features
## Conference Summary Dashboard
Displays a summary of statistics from MySQL and Neo4j, these include:
- Total Attendees
- Total Companies
- Total Sessions
- Total Rooms
- Total Neo4j Connections
