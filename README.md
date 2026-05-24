# AI Real Estate Market Intelligence Platform

AI-powered analytics platform designed to analyze housing trends, pricing behavior, affordability, and inventory movement across Metro Atlanta using automated ETL pipelines, GIS analytics, and interactive business intelligence dashboards.

---

## Tech Stack

Python | Streamlit | SQL | Tableau | BigQuery | Plotly | GIS Analytics

---

## Dashboard Preview

<img width="1512" height="982" alt="Realestate SS" src="https://github.com/user-attachments/assets/766766c6-3965-4db7-b22b-17cc64526b01" />


---

## Business Problem

Real estate professionals and investors often rely on fragmented market data across multiple sources, making it difficult to identify pricing trends, inventory shifts, and investment opportunities efficiently.

---

## Solution

Developed a centralized market intelligence platform integrating synthetic housing and market datasets into automated reporting workflows and interactive dashboards for real-time pricing analysis and geographic market insights.

---

## Key Features

- Automated ETL data pipelines
- Geographic market mapping
- Price-per-square-foot benchmarking
- Affordability analysis
- Inventory trend tracking
- AI-generated market summaries
- Executive-style reporting dashboards

---

## Architecture Overview

CSV/API Data
      ↓
Python ETL Pipelines
      ↓
BigQuery / SQL Warehouse
      ↓
Tableau / Streamlit Dashboards
      ↓
AI Market Insight Reporting

---

## KPI Metrics

- Median Home Price
- Price per Sq Ft
- Inventory Movement
- Affordability Score
- Market Growth Trends
- Regional Demand Analysis

---

## Repository Structure

/data
/dashboard_app
/sql
/etl
/assets
/docs

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Real-Estate-Market-Intelligence-Platform.git
cd AI-Real-Estate-Market-Intelligence-Platform

Create Virtual Environment

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Dashboard
streamlit run app.py
