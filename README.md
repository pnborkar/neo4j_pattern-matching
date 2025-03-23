# Neo4j Pattern Matching for Pharma Supply Chain

This project explores **pattern matching in a pharmaceutical supply chain** using Neo4j. It includes real-world graph queries to identify bottlenecks, supply risks, product dependencies, and demand back-pressure — all modeled within a connected graph of suppliers, raw materials, APIs, products, equipment, and distributors.

---

## 📦 Project Structure

- [`start_pattern_matching.ipynb`](./start_pattern_matching.ipynb):  
  Jupyter Notebook with guided Cypher queries and explanations.
  🔍 Explore Key Questions: 
	•	How does distributor demand flow back to raw material requirements?
	•	Are there APIs that are used in multiple Drug Products and could create a supply bottleneck?
	•	Are there APIs used in multiple Drug Products but supplied by only one supplier?
	•	Which raw materials are used in many products but have limited suppliers?
	•	What is the full supply chain path for a specific product SKU?


- Sample data files and Cypher examples (see notebook for details).

---

## 🚀 Getting Started

### 1. Load the Data into Neo4j
Make sure your Neo4j database is running and the supply chain data is loaded into it. You can do this using:

- The **Neo4j Data Importer**
- Custom Cypher scripts (if available)
- `apoc.load.json()` or Python import scripts

### 2. Open and Run the Notebook
Launch the notebook:

```bash
jupyter notebook start_pattern_matching.ipynb