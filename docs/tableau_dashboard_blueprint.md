# Tableau Dashboard Blueprint

Pages:
1. Executive Market Overview: listings, median sale price, avg DOM, avg PPSF, affordability score.
2. GIS Market Map: latitude/longitude map colored by price_per_sqft and filtered by market/property_type.
3. Affordability & Investment Screener: affordability_score, DOM segment, school_score, crime_index, walk_score.
4. Price Benchmarking: market-level PPSF, sale-to-list ratio, monthly pricing trend.

Recommended Tableau Calculated Fields:
- Sale-to-List Ratio = [sale_price] / [list_price]
- Market Heat Score = (100 - [days_on_market]) * 0.35 + [school_score] * 0.35 + [affordability_score] * 0.30
- Price Tier = IF [sale_price] < 350000 THEN 'Entry' ELSEIF [sale_price] < 600000 THEN 'Move-Up' ELSE 'Luxury' END
