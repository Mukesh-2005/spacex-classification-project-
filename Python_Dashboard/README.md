# 📈 Lab 7: SpaceX Launch Dashboard with Dash

## 📌 Objective
To build an interactive dashboard using Python and Dash that visualizes SpaceX Falcon 9 launch records. This lab combines dropdowns, sliders, and dynamic charts to explore launch success rates and payload relationships across different sites.

## 🛠️ Tools Used
- `Dash`: For building the web-based dashboard
- `Plotly Express`: For creating interactive pie and scatter plots
- `pandas`: For data manipulation and filtering

## 🧩 Dashboard Components

### 🔹 Dropdown Menu
- Allows selection of launch site:
  - `All Sites`
  - `CCAFS LC-40`
  - `VAFB SLC-4E`
  - `KSC LC-39A`
  - `CCAFS SLC-40`

### 🔹 Pie Chart
- Displays:
  - **Total successful launches per site** (when "All Sites" is selected)
  - **Success vs. Failure** for a specific site (when selected)
- Example: For `VAFB SLC-4E`, the chart shows **60% success** and **40% failure**

### 🔹 Payload Range Slider
- Selects payload mass range from **0 to 10,000 kg**
- Dynamically filters data for scatter plot

### 🔹 Scatter Plot
- Shows correlation between **Payload Mass** and **Launch Success**
- Color-coded by `Booster Version Category`
- Updates based on selected site and payload range

## 🔄 Callback Logic
- `site-dropdown` → updates pie chart
- `site-dropdown` + `payload-slider` → updates scatter plot

## 🐞 Debugging Note
- Replaced deprecated `app.run_server()` with `app.run(debug=True)` to fix runtime error

## 🖼️ Dashboard Preview

Below is a screenshot of the interactive dashboard showing launch success and payload analysis for VAFB SLC-4E:

![SpaceX Dashboard Screenshot](dashboard_screenshot.png)

## 📘 What I Learned
- How to build interactive dashboards using Dash and Plotly
- How to connect UI components (dropdowns, sliders) to dynamic visualizations
- How to filter and visualize data based on user input
- How to debug and adapt to API changes in Dash

## 📁 Files in This Folder
- `spacex-dash-app.py`: Full dashboard code
- `spacex_launch_dash.csv`: Dataset used for visualization
- `README.md`: This documentation
- `launch_dashboard.png`: Screenshot of the dashboard

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: September 2025
