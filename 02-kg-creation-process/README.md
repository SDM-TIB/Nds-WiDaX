# Knowledge Graph Creation Process

Once a dataset is inserted in WiDaX-LDM, the extracted metadata  are semantified using the SDM-RDFizer, an interpreter of mapping rules that allows the transformation of (un)structured data into RDF knowledge graphs ([SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)).
The current version of the SDM-RDFizer assumes mapping rules are defined in the RDF Mapping Language ([RML](https://rml.io/specs/rml/)) by Dimou et al.

The Knowledge Graph is going to be a key asset in the project and used to validate metadata, and find, evaluate, and fix interoperability issues that could be inserted during the importation process over different sources and different metadata schemas.

## 🗂️ Folder Structure

| Folder | Description |
|--------|-------------|
| `RDFizer_mappings/` | RML mappings for RDF graph semantification |
