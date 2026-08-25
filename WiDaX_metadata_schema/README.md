# WiDaX Metadata Schema

Nds-WiDaX uses the metadata schema of the Leibniz Data Manager (**[LDM](https://github.com/SDM-TIB/LDM_Docker/)**) to provide a common structure for metadata harvested from research data repositories across Lower Saxony.

This folder contains the schema analysis, entity-relationship diagrams, repository-specific mapping documentation, API references, and integration notes used to define and maintain the WiDaX metadata model.

## 📁 Folder Contents

| Folder | Description |
|--------|-------------|
| `WiDaX_schema_analysis_DOCs/` | Schema diagrams, repository profile mappings, API documentation, and integration notes |
| `images/` | Rendered diagrams used by the project documentation |

---

## 🧩 Metadata Schema Diagrams

The entity-relationship diagrams document the base WiDaX/LDM metadata model and its repository-specific extensions:

| Diagram | Description |
|---------|-------------|
| [`ERD_WIDAX_base.drawio`](WiDaX_schema_analysis_DOCs/ERD_WIDAX_base.drawio) | Base WiDaX metadata schema |
| [`ERD_WIDAX_GOE.drawio`](WiDaX_schema_analysis_DOCs/ERD_WIDAX_GOE.drawio) | Göttingen Research Online |
| [`ERD_WIDAX_LEO.drawio`](WiDaX_schema_analysis_DOCs/ERD_WIDAX_LEO.drawio) | LeoPARD |
| [`ERD_WIDAX_LUH.drawio`](WiDaX_schema_analysis_DOCs/ERD_WIDAX_LUH.drawio) | Leibniz University Hannover |
| [`ERD_WIDAX_OSN.drawio`](WiDaX_schema_analysis_DOCs/ERD_WIDAX_OSN.drawio) | Osnadata |

The base schema Preview:

![WiDaX metadata schema](images/ERD_WIDAX_base.png)

The schema is designed to normalize common dataset metadata such as identifiers, titles, descriptions, creators, licenses, publication dates, subjects, related identifiers, repository information, and resources. Repository-specific import profiles transform source fields into this common structure.

---

