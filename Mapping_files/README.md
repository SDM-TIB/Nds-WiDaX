Nds-WiDaX builds on the Leibniz Data Manager (**[LDM](https://github.com/SDM-TIB/LDM_Docker/)**) – an open, semantics-oriented software service – to enable machine-readable, contextually rich indexing of heterogeneous (meta)data from research data repositories across Lower Saxony.

LDM's Nds-WiDaX instance collects datasets' metadata from Lower Saxony repositories using APIs (more details in (**[documentation](../Plugin-Python/documentation/LowerSaxonyRepositoriesDocumentation.md#2.-repository-profiles-and-technical-specifications)**) and performs the importation following these steps:

1. Json files for each dataset are converted from the source schema into a new file respecting the LDM's metadata schema, allowing a clean importation. This transformation is performed using a declarative mapping language developed by the TIB-SDM group (**[KG Graph Integration API](https://github.com/SDM-TIB/FAIR_RDM_APIs/tree/main/knowledge_graph_managment/knowledge_graph_integration/api)**).

![WiDaX metadata schema](../WiDaX_metadata_schema/images/ERD_WIDAX_base.png)

2. The metadata extracted is semantified using the SDM-RDFizer, an interpreter of mapping rules that allows the transformation of (un)structured data into RDF knowledge graphs (**[SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)**).

![RDFizer architecture](../WiDaX_metadata_schema/images/RDFizer_architecture.png)

# 📁 Mapping files for WiDaX importation

**Folder:** `Mapping_files`

---

## 📦 Contents

In this folder we can find:

- `json_importation_files/Repository Name/json_files_from_source`: JSON files coming directly from repositories' REST APIs or converted to JSON in case of OAI-PMH APIs (XML).
- `json_importation_files/Repository Name/json_files_mapped_to_LDM`: JSON files adapted to the LDM-WiDaX metadata schema.
- `json_mappings`: Mapping files using the declarative mapping language for each repository.
- `RDFizer_mappings`: Mapping files in RML used for metadata semantification.

---

## 🗂️ Folder Structure

| Folder | Description |
|--------|-------------|
| `json_importation_files/` | Source and transformed JSON metadata files per repository |
| `json_mappings/` | Declarative mappings for repository-specific schema conversion |
| `RDFizer_mappings/` | RML mappings for RDF graph semantification |

---
