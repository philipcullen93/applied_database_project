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

2. If installing manually:
      pip install mysql-connector-python neo4j

## Running the Application
1. Ensure MySQL is running.
   Note: If MySQL Server is not connected navigate to Services -> MySQL80 and Start the Service

2. Ensure Neo4j is running.

3. Enter python app.py in the terminal
   Note: The application will confirm that both the MySQL and Neo4j databases are connected.
   
