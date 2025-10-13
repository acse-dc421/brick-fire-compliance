# 🧱 Brick Fire Compliance Ontology (v1.1)

**Brick Fire Compliance Ontology (BFCO)** is a modular extension of the [Brick schema](https://brickschema.org) designed to represent **operational fire-safety assets, hazards, and compliance relations** in buildings.  
It provides a formal vocabulary for describing *in-use fire safety conditions* and enables ontology-based reasoning for automated compliance monitoring.

---

## 🔍 Overview

Traditional Brick focuses on representing building systems (HVAC, lighting, etc.) and static design semantics.  
However, **operational fire safety** introduces dynamic factors such as **obstructions, degraded equipment, and informal modifications** that evolve after building occupancy.  

The Brick Fire Compliance Ontology introduces new classes and relations for modeling such conditions, supporting interoperability between perception-driven inspection data and rule-based compliance reasoning.

---

## 📘 File Structure

```
brick-fire-compliance/
│
├── ontology/
│   └── brick-fire-compliance_1.1.ttl        # Core ontology
│
├── compliance_rules/
│   ├── rule_mapping.json                    # Example compliance queries
│   ├── query_egress_obstruction.sparql
│   └── query_equipment_access.sparql
│
├── examples/
│   ├── example_instances.ttl                # Sample building data (valid)
│   ├── error_example_instances.ttl          # Invalid data sample (for SHACL testing)
│   └── run_example.py                       # Quick demo (planned)
│
├── docs/
│   └── ontology_diagram.png                 # Visual schema diagram
│
├── validation/
│   ├── shacl_validation.ttl                 # SHACL validation shapes
│   └── validate_example.py                  # Executable validation script
│
└── README.md
```


---

## 🧩 Key Features

- **Partial alignment with Brick v1.5+**  
  Maintains compatibility with Brick’s core structure (Location–Equipment–Point) while extending it for fire-safety domains.

- **New semantic layer for operational compliance**  
  Introduces the `Hazard` class with properties like `hazardType` and `affectsEquipment`.

- **Support for rule-based compliance checking**  
  Enables mapping between regulatory clauses and query templates.

- **Extensible and machine-readable**  
  Distributed as a Turtle (TTL) ontology with standard OWL/RDFS constructs.

---

## 🧱 Ontology Structure

The figure below shows the integration between Brick and the fire-compliance extension:

`To be released...`

**Legend:**
- ⚫ Original Brick definitions  
- 🔴 Fire-safety extensions (`haz: namespace`)

Core relationships include:
- `hasHazard` – associates a `Location` with observed `Hazard`
- `affectsEquipment` – links `Hazard` to the `FireAsset` it obstructs
- `connectsTo` – models spatial adjacency for egress reasoning
- `violatesClause` – connects `Hazard` to referenced regulations


---


## ✅ Validation

This module performs **semantic validation** of the Brick Fire Compliance Ontology and its example instance data using SHACL.  
The validation process ensures that all ontology entities and relationships conform to the defined structural and datatype constraints.

---

### ▶️ Run the Validation

Install required dependencies:

```bash
pip install rdflib pyshacl
```

Then execute the validation script:

```bash
cd validation
python validate_example.py
```

---

### 💡 Expected Output

```
------------------------------------------------------------
 Brick Fire Compliance Ontology — SHACL Validation Demo
------------------------------------------------------------

[1] Loading ontology and instance data ...
    ✓ Ontology and instances successfully loaded.

[2] Loading SHACL validation shapes ...
    ✓ SHACL shapes successfully loaded.

[3] Running SHACL validation ...

------------------------------------------------------------
 Validation Summary
------------------------------------------------------------
Conforms: True

Detailed Report:
Validation Report
Conforms: True

Execution complete. ✅
------------------------------------------------------------
```

## 🧠 Integration & Reasoning

- **RDFLib** — Load ontology and instances for local querying.  
- **Owlready2** — Perform reasoning or class-based inference.  
- **PySHACL** — Validate semantic compliance constraints.

These lightweight libraries allow integration into inspection systems or VLM-based hazard recognition pipelines.

---

## 📜 Citation

If you use this ontology, please cite:

> Chen, D. et al. (2025). *Brick Fire Compliance Ontology (v1.1)*.  
> Loughborough University.  
> https://github.com/acse-dc421/brick-fire-compliance

---


## 📘 License

This ontology is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://github.com/BrickSchema/brick/blob/master/LICENSE).

---

## 🏛 Acknowledgements

Developed by **Loughborough University** under the WTW Research Network Technology driven Next Generation Insurance *TECHNGI* program, with contributions to the broader Brick community for enhancing **operational fire-safety representation** in building digital twins.
