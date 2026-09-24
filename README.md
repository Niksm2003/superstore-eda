# Superstore Sales Intelligence Dashboard

An interactive sales analytics dashboard built with Python, Pandas, Plotly, 
and Streamlit — deployed live on Streamlit Cloud.

🔗 **Live Dashboard:** https://niksm2003-superstore-sales.streamlit.app

---

## Overview

This project performs end-to-end exploratory data analysis (EDA) on the 
Kaggle Superstore Sales dataset (9,994 orders, 4 regions, 3 product 
categories, 2014–2017) and presents the findings as an interactive, 
filterable dashboard.

The dashboard allows users to filter by Region, Product Category, and Year — 
all charts and KPIs update dynamically based on the selected filters.

---

## Dashboard Sections

### 1. Key Metrics
Real-time KPI cards showing:
- Total Revenue
- Net Profit and Profit Ratio
- Total Orders
- Average Profit Margin

### 2. Category Performance
- Revenue vs Profit comparison across Furniture, Office Supplies, Technology
- Revenue breakdown across all 17 Sub-Categories

### 3. Regional Analysis
- Revenue and Profit by Region (East, West, Central, South)
- Revenue share by Region (donut chart)
- Revenue by Customer Segment (Consumer, Corporate, Home Office)

### 4. Sales Trend
- Monthly Revenue and Profit trend across 2014–2017
- Identifies seasonal peaks and growth patterns

### 5. Product Performance and Discount Impact
- Top 10 most profitable products
- Scatter plot showing the relationship between discount rate and profit
- Key finding: orders with discounts above 30% result in losses 80%+ of the time

### 6. Shipping Analysis
- Revenue by Shipping Mode (Standard, Second Class, First Class, Same Day)
- Average fulfilment time by Shipping Mode

---

## Key Findings

- **Technology** is the highest revenue category ($836K) but **Office Supplies** 
  has the strongest profit margins
- The **West** region leads in total revenue; the **East** region delivers 
  the highest profit
- **Phones** and **Chairs** are the top two sub-categories by revenue 
  ($330K and $328K respectively)
- Heavy discounting (>30%) is the primary driver of margin erosion — 
  particularly in the Furniture category
- **Standard Class** shipping accounts for the majority of orders but 
  **Same Day** shipping has the fastest fulfilment time

---

## Dataset

- **Source:** Kaggle Superstore Sales Dataset
- **Download:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
- **Size:** 9,994 orders · 21 features
- **Period:** January 2014 – December 2017
- **Regions:** East, West, Central, South
- **Categories:** Furniture, Office Supplies, Technology

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, aggregation |
| Plotly | Interactive charts and visualisations |
| Streamlit | Dashboard framework and deployment |
| Streamlit Cloud | Free hosting and deployment |

---

## Project Structure
superstore-eda/
│
├── app.py # Main Streamlit dashboard application
│ # - Top filter bar (Region, Category, Year)
│ # - KPI metric cards
│ # - Category performance charts
│ # - Regional analysis (bar + donut charts)
│ # - Monthly sales trend (line chart)
│ # - Product performance (bar chart)
│ # - Discount impact analysis (scatter plot)
│ # - Shipping analysis (bar charts)
│
├── Sample - Superstore.csv # Dataset (9,994 orders, 21 features)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## How to Run Locally

1. Clone this repository
git clone https://github.com/Niksm2003/superstore-eda.git

2. Navigate to the project folder
cd superstore-eda

3. Install dependencies
pip install -r requirements.txt

4. Run the dashboard
streamlit run app.py

5. Open your browser at `http://localhost:8501`

---

## Requirements
streamlit
pandas
plotly
openpyxl

---

## Live Demo

🔗 **https://niksm2003-superstore-sales.streamlit.app**

---

*Built by Nikhil Mishra · [github.com/Niksm2003](https://github.com/Niksm2003)*
