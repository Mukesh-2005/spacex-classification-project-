# 📊 Lab 5: Exploratory Data Analysis and Feature Engineering

## 📌 Objective
To visually explore relationships in the Falcon 9 launch dataset and prepare features for supervised learning. This lab combines statistical plotting with one-hot encoding to transform categorical variables into machine-readable format.

## 🛠️ Tools Used
- `matplotlib` and `seaborn`: For bar plots, scatter plots, box plots, and line charts
- `pandas`: For data manipulation and feature engineering
- `get_dummies`: For one-hot encoding categorical columns

## 🔍 Key Activities

### 🔹 Data Visualization Tasks
1. **Flight Number vs. Launch Site**  
   - Bar plot showing how launch frequency varies across sites.

2. **Payload Mass vs. Launch Site**  
   - Scatter plot to explore payload distribution across different launch pads.

3. **Success Rate by Orbit Type**  
   - Bar plot showing proportion of successful landings per orbit category.

4. **Flight Number vs. Orbit Type**  
   - Scatter plot to examine if certain orbits are associated with specific launch phases.

5. **Payload Mass vs. Orbit Type**  
   - Box plot to compare payload distributions across orbit categories.

6. **Yearly Launch Success Trend**  
   - Line plot showing how Falcon 9 success rates evolved over time.

### 🔹 Feature Engineering
- Applied `pd.get_dummies()` to convert categorical columns into binary indicators:
  - `Orbit`, `LaunchSite`, `LandingPad`, `Serial`
- Resulted in **80+ columns**.
- Ensured all columns were converted to `float64` for compatibility with machine learning models.

## 📘 What I Learned
- How to visualize categorical vs. numerical relationships using appropriate plot types
- How to interpret trends and distributions visually
- How to encode categorical variables using one-hot encoding
- How to prepare a high-dimensional feature matrix for classification tasks

## 📁 Files in This Folder
- `lab5_visualization.ipynb`: Full notebook with plots and feature engineering
- `README.md`: This documentation

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: November 2025
