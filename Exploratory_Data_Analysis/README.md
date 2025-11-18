# 🧪 Lab 3: Exploratory Data Analysis with SQL (SQLite)

## 📌 Objective
To perform exploratory data analysis (EDA) on the Falcon 9 launch dataset using SQL within a Jupyter notebook environment. This lab focused on querying structured data using SQL syntax and validating insights obtained from previous pandas-based analysis.

## 🛠️ Tools Used
- `sqlalchemy`: To create and manage a SQLite database connection
- `ipython-sql`: To run SQL queries directly in notebook cells using `%%sql` magic
- `prettytable`: To display SQL query results in a clean tabular format

## 🔍 Key Activities
- Loaded the wrangled dataset from Lab 2 into a SQLite database
- Executed SQL queries to explore:
  - **Launch site distribution**
  - **Orbit type frequencies**
  - **Landing outcome categories**
  - **Payload mass statistics**
  - **Temporal trends** (e.g., launches by year) etc.,
- Mapped landing outcomes to binary success/failure classes using SQL logic
- Compared SQL-based summaries with pandas outputs for consistency


## 📘 What I Learned
- How to use SQL for structured data exploration inside Jupyter
- How to translate pandas logic into SQL queries
- How to validate and summarize categorical and numerical features using SQL
- The value of combining SQL and Python for flexible, reproducible analysis

## 📁 Files in This Folder
- `lab3_notebook.ipynb`: Full SQL-based EDA notebook
- `falcon9.sqlite`: SQLite database file
- `README.md`: This documentation

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: September 2025
