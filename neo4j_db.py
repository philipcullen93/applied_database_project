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