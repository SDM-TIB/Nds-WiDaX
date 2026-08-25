Nds-WiDaX builds on the Leibniz Data Manager (**[LDM](https://github.com/SDM-TIB/LDM_Docker/)**) – an open, semantics-oriented software service – to enable machine-readable, contextually rich indexing of heterogeneous (meta)data from research data repositories across Lower Saxony.
The Leibniz Data Manager (LDM) is an open source and free web-based application for Research Data Management (RDM). LDM delivers different distributions to best fit the specific requirements of various customers, e.g., institutes and research groups performing RDM in various scientific disciplines. The LDM distributions are designed, maintained, and curated by TIB and L3S.

In this folder we can find the code and evolution of the LDM's TIBimport plugin performing the importations and updates inside the WiDaX instance.

# 📁 Relevant Documents in TIBimport plugin:

**Folder:** `ckanext-TIBimport\ckanext\tibimport`

---

## 🔧 Core Logic

| File | Description |
|------|-------------|
| `logic2.py` | Defines the importer logic |

---

## 📋 Importation Profiles

> One profile per repository:

| Profile File | Repository |
|--------------|------------|
| `LUH_CKAN_API_ParserProfile.py` | LUH CKAN API |
| `GOETTINGEN_ParserProfile.py` | Göttingen |
| `LEOPARD_ParserProfile.py` | Leopard |
| `LEUPHANA_ParserProfile.py` | Leuphana |
| `OSNADATA_ParserProfile.py` | Osnadata |

---

## 📚 Documentation

**Complete Documentation:** [`documentation/README.md`](documentation/README.md)

The documentation directory contains comprehensive guides covering:

| Topic | Description |
|-------|-------------|
| 🖥️ **System Documentation** | Technical specifications, architecture, and API details |
| 👤 **User Documentation** | User guides and operational procedures |
| 🎓 **Lower Saxony Repositories Documentation** | Specialized documentation for academic repository integrations |
