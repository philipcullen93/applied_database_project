# Neo4j Database Functions

# Import Neo4j GraphDatabase package
from neo4j import GraphDatabase


# Create and return a Neo4j database driver
def get_driver():
    return GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "neo4jneo4j")
    )


# Test Neo4j database connection
def test_neo4j_connection():
    try:
        driver = get_driver()

        # Verify Neo4j server connectivity
        driver.verify_connectivity()

        driver.close()
        return True

    # Display connection error if connection fails
    except Exception as e:
        print("Neo4j connection error:", e)
        return False


# Retrieve attendees connected to a selected attendee
def get_connected_attendees(attendee_id):
    driver = get_driver()

    # Cypher query to retrieve connected attendees
    query = """
        MATCH (a:Attendee {AttendeeID: $attendee_id})-[:CONNECTED_TO]-(b:Attendee)
        RETURN b.AttendeeID
        ORDER BY b.AttendeeID;
    """

    with driver.session() as session:

        # Execute query using supplied attendee ID
        result = session.run(query, attendee_id=int(attendee_id))

        # Store connected attendee IDs in a list
        connections = [record["b.AttendeeID"] for record in result]

    driver.close()
    return connections


# Check if a connection already exists between two attendees
def connection_exists(attendee_id_1, attendee_id_2):
    driver = get_driver()

    # Cypher query checks both directions of relationship
    query = """
        MATCH (a:Attendee {AttendeeID: $id1})-[:CONNECTED_TO]-(b:Attendee {AttendeeID: $id2})
        RETURN COUNT(*) AS connectionCount
    """

    with driver.session() as session:

        # Execute query using supplied attendee IDs
        result = session.run(
            query,
            id1=int(attendee_id_1),
            id2=int(attendee_id_2)
        )

        count = result.single()["connectionCount"]

    driver.close()

    # Return True if connection exists
    return count > 0


# Create a new attendee connection in Neo4j
def add_connection(attendee_id_1, attendee_id_2):
    driver = get_driver()

    # MERGE prevents duplicate nodes and relationships
    query = """
        MERGE (a:Attendee {AttendeeID: $id1})
        MERGE (b:Attendee {AttendeeID: $id2})
        MERGE (a)-[:CONNECTED_TO]-(b);
    """

    with driver.session() as session:

        # Execute Cypher query
        session.run(query, id1=int(attendee_id_1), id2=int(attendee_id_2))

    driver.close()

# Retrieve total number of attendee connections
def get_total_connections():
    driver = get_driver()

    query = """
        MATCH ()-[r:CONNECTED_TO]-()
        RETURN COUNT(r) AS totalConnections
    """

    with driver.session() as session:
        result = session.run(query)
        total = result.single()["totalConnections"]

    driver.close()

    return total