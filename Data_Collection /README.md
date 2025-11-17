# 🚀 Lab 1: Data Collection with SpaceX API

## 📌 Objective
To collect and structure SpaceX launch data using REST API calls, focusing specifically on Falcon 9 missions. The goal was to extract only the most relevant features for downstream analysis and machine learning.

## 🔍 Key Activities
- Accessed the SpaceX public API endpoints using Python’s `requests` library.
- Retrieved launch data in JSON format and normalized it using `json_normalize`.
- Observed that the raw JSON data was deeply nested and contained many irrelevant or redundant columns.
- Carefully filtered and selected only the necessary fields from each nested object:
  - From the `rocket` object: extracted the **booster version name**.
  - From the `payload` object: extracted the **payload mass** and **orbit**.
  - From the `launchpad` object: extracted the **launch site name**, **longitude**, and **latitude**.
  - From the `cores` object: extracted detailed landing information including:
    - **Landing outcome**, **landing type**, **number of flights**, **gridfins used**, **core reused**, **landing legs**, **landing pad**, **block number**, **reuse count**, and **core serial**.
- Stored all extracted values in Python lists and assembled them into a clean pandas DataFrame.
- Filtered the dataset to include only **Falcon 9** launches.
- Handled **5 missing values** in the `PayloadMass` column by replacing them with the **mean payload mass**.
- Final dataset included the following columns:

```python
['FlightNumber', 'Date', 'BoosterVersion', 'PayloadMass', 'Orbit',
 'LaunchSite', 'Outcome', 'Flights', 'GridFins', 'Reused', 'Legs',
 'LandingPad', 'Block', 'ReusedCount', 'Serial', 'Longitude', 'Latitude']
```
## 📘 What I Learned
- How to interact with REST APIs and parse complex nested JSON structures.
- The importance of feature selection when dealing with high-dimensional or messy data.
- How to merge and align data from multiple API endpoints to build a unified dataset.
- Practical experience in handling missing values and preparing data for machine learning.
- Gained deeper understanding of the SpaceX launch architecture, especially Falcon 9’s components and mission metadata.
## 📁 Files in This Folder
- lab1_notebook.ipynb: Full code for API calls, data extraction, filtering, and cleaning
- README.md: This documentation.

