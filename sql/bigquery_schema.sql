-- BigQuery schema for AI Real Estate Market Intelligence Platform
CREATE OR REPLACE TABLE real_estate.property_listings (
  property_id STRING, list_date DATE, market STRING, property_type STRING, beds INT64, baths FLOAT64, sqft INT64, age_years INT64,
  lot_acres FLOAT64, school_score INT64, crime_index FLOAT64, walk_score INT64, median_household_income INT64, mortgage_rate FLOAT64,
  list_price INT64, sale_price INT64, days_on_market INT64, sold_flag BOOL, latitude FLOAT64, longitude FLOAT64, price_per_sqft FLOAT64,
  affordability_score FLOAT64, inventory_risk_segment STRING
);

CREATE OR REPLACE VIEW real_estate.market_kpis AS
SELECT market, DATE_TRUNC(list_date, MONTH) AS month, COUNT(*) AS listings, APPROX_QUANTILES(sale_price, 100)[OFFSET(50)] AS median_sale_price,
AVG(price_per_sqft) AS avg_ppsf, AVG(days_on_market) AS avg_dom, AVG(affordability_score) AS avg_affordability
FROM real_estate.property_listings
WHERE sold_flag = TRUE
GROUP BY market, month;
