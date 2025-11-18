# 🌐 Lab 3: Web Scraping SpaceX Launch Data

## 📌 Objective
To extract structured SpaceX Falcon 9 launch data from a public HTML table using Python-based web scraping techniques. This lab demonstrates how to parse complex HTML structures and convert them into clean, tabular data.

## 🛠️ Tools Used
- `requests`: To fetch the HTML content from the target URL
- `BeautifulSoup`: To parse and navigate the HTML DOM
- `pandas`: To store and manipulate the extracted data

## 🔍 Key Activities
- Sent an HTTP request to the target URL and retrieved the HTML content
- Parsed the HTML using `BeautifulSoup` to locate the launch history table
- Extracted column headers from the `<th>` tags
- Iterated through each `<tr>` row in the table:
  - Verified that the row contained a valid **flight number**
  - Extracted:
    - `Flight Number`, `Date`, `Time`
    - `Booster Version`, `Launch Site`, `Payload`
    - `Payload Mass`, `Orbit`, `Customer`
    - `Launch Outcome`, `Booster Landing`
- Used helper functions like `date_time()`, `booster_version()`, and `landing_status()` to clean and format values
- Stored all extracted values in a dictionary and converted it into a pandas DataFrame
- Filtered the dataset to include only **Falcon 9** launches
- Saved the final structured data to CSV for downstream analysis

## 📘 What I Learned
- How to navigate and extract structured data from complex HTML tables
- How to use conditional logic to filter valid rows (e.g., rows with numeric flight numbers)
- How to use helper functions to clean and standardize scraped values
- How to build a reproducible scraping pipeline using Python

## 📁 Files in This Folder
- `lab3_webscraping.ipynb`: Full notebook with scraping, parsing, and cleaning logic
- `scraped_launch_data.csv`: Final cleaned dataset 
- `README.md`: This documentation

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: September 2025
