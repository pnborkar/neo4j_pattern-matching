# Neo4j Pattern Matching for Pharma Supply Chain

This project explores **pattern matching in a pharmaceutical supply chain** using Neo4j. It includes real-world graph queries to identify bottlenecks, supply risks, product dependencies, and demand back-pressure — all modeled within a connected graph of suppliers, raw materials, APIs, products, equipment, and distributors.

---

## 📦 Project Structure

- [`start_pattern_matching.ipynb`](./start_pattern_matching.ipynb):  
  Jupyter Notebook with guided Cypher queries and explanations.
  🔍 Explore Key Questions: 
    1. Identify Raw Materials with limited Suppliers
    2. Identify APIs Used in Multiple Drug Products with Potential Supply Risk
    3. Identify Single-Supplier APIs with Broad Product Impact
    4. How Does Distributor Demand Flow Back to Raw Material Requirements?




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