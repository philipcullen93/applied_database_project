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

## New Features/Innovations
### Conference Summary
Displays a summary of statistics from MySQL and Neo4j, these include:
- Total Attendees
- Total Companies
- Total Sessions
- Total Rooms
- Total Neo4j Connections

### Recommend Connections
Recommends possible attendee connections based on shared session attendance while excluding attendees already connected in the Neo4j graph.

This combines several pieces of data:
1. MySQL session registration data
2. Neo4j relationship data
3. Python filtering logic

# References

## General Python / Database References

- Python Official Documentation  
  https://docs.python.org/3/

- MySQL Connector/Python Documentation  
  https://dev.mysql.com/doc/connector-python/en/

- Neo4j Python Driver Documentation  
  https://neo4j.com/docs/python-manual/current/

## Menu Option 1 - View Speakers & Sessions

Used SQL JOIN queries to retrieve related data from multiple tables.

References:
- https://www.w3schools.com/sql/sql_join.asp
- https://dev.mysql.com/doc/refman/8.0/en/join.html

## Menu Option 2 - View Attendees by Company

Used INNER JOIN queries across attendee, company, registration, session, and room tables.

References:
- https://www.w3schools.com/sql/sql_join_inner.asp
- https://realpython.com/python-mysql/

## Menu Option 3 - Add New Attendee

Used SQL INSERT statements and Python exception handling.

References:
- https://www.w3schools.com/sql/sql_insert.asp
- https://docs.python.org/3/tutorial/errors.html

## Menu Option 4 - View Connected Attendees

Used Neo4j Cypher MATCH queries and graph traversal relationships.

References:
- https://neo4j.com/docs/cypher-manual/current/clauses/match/
- https://neo4j.com/developer/graph-database/

## Menu Option 5 - Add Attendee Connection

Used Neo4j MERGE statements to create nodes and relationships while preventing duplicates.

References:
- https://neo4j.com/docs/cypher-manual/current/clauses/merge/
- https://neo4j.com/docs/python-manual/current/query-simple/

## Menu Option 6 - View Rooms

Used cached room data stored in Python variables to prevent unnecessary database reads.

References:
- https://docs.python.org/3/tutorial/datastructures.html
- https://realpython.com/python-variables/

## Menu Option 7 - Conference Summary

Used aggregate SQL functions and Neo4j relationship counting.

References:
- https://www.w3schools.com/sql/sql_count_avg_sum.asp
- https://neo4j.com/docs/cypher-manual/current/functions/aggregating/

## Menu Option 8 - Recommend Connections

Used recommendation logic based on shared conference sessions and filtering existing Neo4j relationships.

References:
- https://neo4j.com/developer/graph-data-science/recommendations/
- https://www.w3schools.com/sql/sql_distinct.asp
