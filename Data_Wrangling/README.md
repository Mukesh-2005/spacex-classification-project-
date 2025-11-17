# 🧹 Lab 2: Data Wrangling and Preprocessing

## 📌 Objective
To clean, transform, and prepare the Falcon 9 launch dataset for exploratory analysis and supervised classification. This lab focused on handling missing values, converting data types, engineering features, and assigning binary labels for mission outcomes.

## 🔍 Key Activities
- Loaded the cleaned dataset from Lab 1 (`launch_data.csv`) using `pandas`.
- Verified and converted data types:
  - `Date` → `datetime`
  - Boolean-like columns (`GridFins`, `Reused`, `Legs`) → `int` (0 or 1)
- Created new features:
  - Extracted **year** from `Date`
  - Engineered a binary **Success** column from `Outcome`
- Renamed columns for clarity (e.g., `BoosterVersion` → `Booster`)
- Reordered columns to group launch metadata, payload, and landing outcome

## 📊 Launch Site Distribution (Falcon 9 Only)
| Launch Site | Launched |
|------------|--------|
|CCAFS SLC 40 |   55 |
|KSC LC 39A   |   22 |
|VAFB SLC 4E  |  13  |


## 🧠 Outcome Mapping Logic
Each mission’s landing outcome was categorized based on the `Outcome` field:

- `<code>True Ocean</code>` → Successful landing in ocean  
- `<code>False Ocean</code>` → Failed ocean landing  
- `<code>True RTLS</code>` → Successful ground pad landing  
- `<code>False RTLS</code>` → Failed ground pad landing  
- `<code>True ASDS</code>` → Successful drone ship landing  
- `<code>False ASDS</code>` → Failed drone ship landing  
- `<code>None ASDS</code>` and `<code>None None</code>` → No landing / failure

## 🎯 Binary Classification Mapping
To prepare for supervised learning, outcomes were mapped to binary classes:

- **Class 1 (Success):**  
  `{True ASDS, True RTLS, True Ocean}`  
- **Class 0 (Failure):**  
  `{False ASDS, False RTLS, False Ocean, None ASDS, None None}`

### Outcome Class Distribution
| Class | Total Outcome |
|-------|--------------|
|1   | 60 |
|0   | 30 |


## 📘 What I Learned
- How to transform raw categorical outcomes into binary labels for classification
- How to interpret and encode domain-specific logic (e.g., landing types)
- How to inspect and summarize categorical distributions for launch sites and orbits
- The importance of clean, consistent formatting for downstream modeling

## 📁 Files in This Folder
- `lab2_notebook.ipynb`: Full code for data wrangling and preprocessing
- `wrangled_data.csv`: Final dataset after transformation (if included)
- `README.md`: This documentation

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: September 2025
