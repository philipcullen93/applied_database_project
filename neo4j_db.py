from neo4j import GraphDatabase

def get_driver():
    return GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "neo4jneo4j")
    )

def test_neo4j_connection():
    try:
        driver = get_driver()
        driver.verify_connectivity()
        driver.close()
        return True
    except Exception as e:
        print("Neo4j connection error:", e)
        return False

def get_connected_attendees(attendee_id):
    driver = get_driver()

    query = """
        MATCH (a:Attendee {AttendeeID: $attendee_id})-[:CONNECTED_TO]-(b:Attendee)
        RETURN b.AttendeeID
        ORDER BY b.AttendeeID;
    """

    with driver.session() as session:
        result = session.run(query, attendee_id=int(attendee_id))
        connections = [record["b.AttendeeID"] for record in result]

    driver.close()
    return connections