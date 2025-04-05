# Olympics 2024 Relational Database System 🏅

This repository contains the complete end-to-end development of a **relational database system** for the **Olympic Games 2024**, developed for the ISYS5008 (Database Systems) unit at Curtin University.

It includes:
- 📐 Database design (ER diagrams, relational schema, normalization)
- 🛠️ Full implementation in **MySQL 8.0** with over 10,000 real-world records
- ⚙️ Advanced features: procedures, triggers, views, integrity constraints
- 🐍 Python 3 integration using MySQL connector
- 📄 Detailed documentation and deployment-ready SQL scripts

---

## 🎯 Project Objective

- Model a real-world relational database from scratch based on original Olympic data
- Use SQL to extract insights using both basic and advanced queries
- Enforce data integrity using stored procedures and triggers
- Enable live data interactions through a Python3 interface

---

## 🗃️ Key Features

### 📐 Design & Modeling
- Created ER Diagram in Chen’s Notation ([LucidChart Link](https://lucid.app/lucidchart/fa774a20...))
- Relational schema normalized to 3NF
- Entity sets: Athletes, Events, Coaches, Countries, Teams, Medals, Participation, Venues, Disciplines

### 🔍 SQL Query Highlights
#### Basic Queries:
- Find all athletes born after 2005
- List gold medal winners
- Search athletes by name or country

#### Advanced Queries:
- Top countries by medal count
- Venue-based event aggregation
- Events with >50 athlete participation

### ⚙️ Advanced SQL Features
- ✅ **Stored Procedures**: AddMedalEntry, GetCountryMedalCount
- 🔁 **Triggers**: Validate athlete DOB and gender, prevent duplicate event inserts
- 👁 **Views**: Top 10 events by participation

### 🐍 Python 3 Integration
- Established MySQL connection via `mysql-connector-python`
- Executed all queries through `.py` scripts
- Insert/update/delete operations controlled via Python terminal scripts

---

## 🔗 Documentation

| File | Description |
|------|-------------|
| `docs/ZaidiSyed_20972008_DbSReport2024.pdf` | Full technical report and analysis |
| `docs/ZaidiSyed_20972008_DbSUserGuide2024.pdf` | Step-by-step database setup guide |
| `sql_files/*.sql` | Source files for schema, queries, procedures |
| `python_files/*.py` | Python scripts for DB connectivity and manipulation |

---

## 🧠 Learnings

- Database architecture & design principles
- Advanced MySQL scripting (views, procedures, triggers)
- Data cleaning using Excel/VLOOKUP for referential integrity
- Automation via Python integration on Linux (VMWare) environment

---

## 👤 Author

**Syed Muhammad Ahmed Zaidi**  


---

## 📄 License
For educational purposes only. Reproduction or use in commercial environments requires written permission.

---
