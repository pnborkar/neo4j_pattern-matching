
from neo4j import GraphDatabase
import json

# === CONFIGURE YOUR TARGET NEO4J AURA INSTANCE ===
NEO4J_URI = "neo4j+s://<your-aura-instance-id>.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your-password"

# === LOAD YOUR JSON DATA ===
with open("your_data.json", "r") as f:
    graph_data = json.load(f)

# === CONNECT TO NEO4J ===
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# === IMPORT FUNCTION ===
def import_graph(tx, node_data, rel_data):
    # Create nodes
    for node in node_data:
        labels = ":".join(node["_labels"])
        properties = {k: v for k, v in node.items() if not k.startswith("_")}
        query = f"MERGE (n:{labels} {{id: $id}}) SET n += $props"
        tx.run(query, id=node["id"], props=properties)

    # Create relationships
    for rel in rel_data:
        query = f'''
        MATCH (a {{id: $start_id}}), (b {{id: $end_id}})
        MERGE (a)-[r:{rel["_type"]}]->(b)
        SET r += $props
        '''
        tx.run(query,
               start_id=rel["_start"],
               end_id=rel["_end"],
               props={k: v for k, v in rel.items() if not k.startswith("_")})

# === RUN IMPORT ===
with driver.session() as session:
    for entry in graph_data:
        node_data = entry.get("nodes", [])
        rel_data = entry.get("relationships", [])
        session.write_transaction(import_graph, node_data, rel_data)

print("✅ Data import to Neo4j Aura completed.")
