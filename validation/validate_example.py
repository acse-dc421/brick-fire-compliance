"""
validate_example.py
------------------------------------------------------------
Semantic validation demo for the Brick Fire Compliance Ontology (BFCO)
------------------------------------------------------------
This script performs SHACL-based validation using pySHACL.

It loads:
  • Core ontology (ontology/brick-fire-compliance_1.1.ttl)
  • Example instance data (examples/example_instances.ttl)
  • SHACL shapes (shacl/validation_shapes.ttl)

It then runs semantic validation to check compliance with
the defined ontology-level and operational fire-safety constraints.

Dependencies:
    pip install rdflib pyshacl
------------------------------------------------------------
"""

import sys
from rdflib import Graph
from pyshacl import validate

# ---------------------------------------------------------------------
# 1. Load ontology and data
# ---------------------------------------------------------------------

print("------------------------------------------------------------")
print(" Brick Fire Compliance Ontology — SHACL Validation Demo")
print("------------------------------------------------------------\n")

g_data = Graph()
g_shapes = Graph()

try:
    print("[1] Loading ontology and instance data ...")
    g_data.parse("ontology/brick-fire-compliance_1.1.ttl", format="turtle")
    g_data.parse("examples/example_instances.ttl", format="turtle") # valid example
    # g_data.parse("error_example_instances.ttl", format="turtle") # Invalid example
    print("    ✓ Ontology and instances successfully loaded.\n")
except Exception as e:
    print("    ✗ Failed to load data: ", e)
    sys.exit(1)

try:
    print("[2] Loading SHACL validation shapes ...")
    g_shapes.parse("validation_shapes.ttl", format="turtle")
    print("    ✓ SHACL shapes successfully loaded.\n")
except Exception as e:
    print("    ✗ Failed to load shapes: ", e)
    sys.exit(1)

# ---------------------------------------------------------------------
# 2. Run SHACL validation
# ---------------------------------------------------------------------

print("[3] Running SHACL validation ...\n")

try:
    conforms, report_graph, report_text = validate(
        data_graph=g_data,
        shacl_graph=g_shapes,
        inference="rdfs",
        abort_on_first=False,
        meta_shacl=False,
        advanced=True,
        debug=False,
    )
except Exception as e:
    print("    ✗ Validation failed to execute:", e)
    sys.exit(1)

# ---------------------------------------------------------------------
# 3. Display summary results
# ---------------------------------------------------------------------

print("------------------------------------------------------------")
print(" Validation Summary")
print("------------------------------------------------------------")

print(f"Conforms: {conforms}")
print("\nDetailed Report:")
print(report_text)

# ---------------------------------------------------------------------
# 4. Save report (optional)
# ---------------------------------------------------------------------

output_path = "validation_report.ttl"
try:
    with open(output_path, "w", encoding="utf-8") as f:
      f.write(report_graph.serialize(format="turtle"))

    print(f"\n[4] Validation report saved to: {output_path}")
except Exception as e:
    print("    ⚠ Could not save report:", e)

print("\nExecution complete. ✅")
print("------------------------------------------------------------")
