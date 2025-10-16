"""
Brick Fire Compliance Ontology — Regulatory Clause Demo
--------------------------------------------------------
This script demonstrates clause-to-query compliance checking.
It loads regulatory mappings, executes SPARQL templates,
and reports violations linked to specific compliance clauses.
"""

import json
from rdflib import Graph

# ------------------------------------------------------------
# [1] Load ontology and instance data
# ------------------------------------------------------------
g = Graph()
g.parse("ontology/brick-fire-compliance_1.1.ttl", format="turtle")
g.parse("examples/example_instances.ttl", format="turtle")

print("✓ Ontology and instance data loaded.\n")

# ------------------------------------------------------------
# [2] Load clause–query mapping
# ------------------------------------------------------------
with open("compliance_rules/rule_mapping.json", "r", encoding="utf-8") as f:
    clause_map = json.load(f)

print("Loaded regulatory mapping:")
for cq, meta in clause_map.items():
    print(f"  {cq} → {meta['reference']}")

# ------------------------------------------------------------
# [3] Execute each compliance query
# ------------------------------------------------------------
for cq_id, meta in clause_map.items():
    print("\n------------------------------------------------------------")
    print(f"Running {cq_id}: {meta['reference']}")
    print(f"Rule: {meta['description']}")

    query_path = f"compliance_rules/{meta['query_file']}"
    with open(query_path, "r", encoding="utf-8") as qf:
        query_str = qf.read()

    results = g.query(query_str)
    if len(results) == 0:
        print("✅ No violations detected.")
    else:
        print("⚠ Violations found:")
        for row in results:
            loc = row.get("loc")
            hazType = row.get("hazType").split("#")[-1]
            desc = row.get("desc")
            print(f" - Location: {loc} | Hazard: {hazType} | Description: {desc}")

print("\n------------------------------------------------------------")
print("Compliance audit complete ✅")
