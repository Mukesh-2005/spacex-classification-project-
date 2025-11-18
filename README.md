# 🚀 SpaceX Falcon 9 Classification Project

This repository documents my hands-on labs from the Coursera Data Science Capstone, focused on classifying SpaceX Falcon 9 launch outcomes. Each folder represents a modular lab session, covering the full data science pipeline — from data collection to dashboard deployment.

## 📚 Project Overview

The goal of this project is to predict the success of SpaceX Falcon 9 launches using historical data. I explored multiple stages of the workflow including API calls, web scraping, SQL-based EDA, geospatial mapping, and supervised machine learning.

## 🧪 Lab Breakdown

| Lab | Description |
|-----|-------------|
| [**1. Data Collection**](Data_Collection/) | Collected Falcon 9 launch data using REST API calls, extracting relevant features for analysis |
| [**2. Data Wrangling**](Data_Wrangling/) | Cleaned and transformed the dataset, handled missing values, engineered features, and labeled outcomes |
| [**3. Web Scraping**](Data_Collection/) | Parsed HTML tables to extract structured launch data using BeautifulSoup |
| [**4. EDA (SQL)**](Exploratory_Data_Analysis/) | Queried launch data using SQL syntax in Jupyter to validate insights |
| [**5. EDA (Visualization)**](Exploratory_Data_Analysis/) | Explored relationships using statistical plots and prepared features for modeling |
| [**6. Location Analysis**](Location_Analysis_with_Folium/) | Mapped launch sites using Folium and calculated distances to key geographic features |
| [**7. Dashboarding**](Python_Dashboard/) | Built an interactive Dash app with dropdowns, sliders, and dynamic charts |
| [**8. Model Evaluation**](Python_Dashboard/) | Trained and compared Logistic Regression, SVM, Decision Tree, and KNN classifiers on launch data |

## 📸 Visual Previews

### 🗺️ Folium Map
![Folium Map](https://github.com/Mukesh-2005/spacex-classification-project-/blob/main/images/Screenshot%202025-11-18%20234714.png?raw=true)


## 🧠 Skills Practiced

- REST API integration
- Web scraping with BeautifulSoup
- Data wrangling and feature engineering
- SQL-based analysis in Jupyter
- Geospatial visualization with Folium
- Interactive dashboarding with Dash
- Supervised learning with scikit-learn

## 📊 Final Outputs

- **Interactive Dashboard**: Visualizes launch success rates by payload, site, and booster version
![Dash Dashboard](https://github.com/Mukesh-2005/spacex-classification-project-/blob/main/images/Screenshot%202025-11-18%20235324.png?raw=true)
- **Model Comparison**: Evaluates four classifiers on unseen test data

## 📁 Repository Structure

- `Data_Collection/`
- `Data_Wrangling/`
- `Exploratory_Data_Analysis/`
- `Location_Analysis_with_Folium/`
- `Python_Dashboard/`
- `LICENSE`
- `README.md`

Each folder contains a dedicated README explaining the lab’s goals, methods, and outcomes.

## 📜 License

This project is licensed under the MIT License.

## 🙋‍♂️ About Me

I’m Mukesh, a BSc Data Science student passionate about blending machine learning with geospatial insights. This project reflects my journey through Coursera’s Data Science Capstone and my commitment to building reproducible, real-world solutions.
