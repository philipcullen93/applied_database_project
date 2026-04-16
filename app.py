from mysql_db import test_mysql_connection
from neo4j_db import test_neo4j_connection

def main():
    if test_mysql_connection():
        print("MySQL server connected ✔")
    else:
        print("MySQL connection failed ❌")

    if test_neo4j_connection():
        print("Neo4j connected ✔")
    else:
        print("Neo4j connection failed ❌")

if __name__ == "__main__":
    main()