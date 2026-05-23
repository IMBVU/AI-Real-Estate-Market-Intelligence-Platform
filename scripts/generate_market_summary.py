import pandas as pd

df = pd.read_csv("data/synthetic_atlanta_housing_records.csv", parse_dates=["list_date"])
latest = df[df["list_date"] >= df["list_date"].max() - pd.Timedelta(days=90)]
summary = latest.groupby("market").agg(
    listings=("property_id","count"),
    median_price=("sale_price","median"),
    median_ppsf=("price_per_sqft","median"),
    avg_dom=("days_on_market","mean"),
    affordability=("affordability_score","mean")
).sort_values("median_price", ascending=False)

for market, row in summary.head(10).iterrows():
    print(f"{market}: median price ${row.median_price:,.0f}, ${row.median_ppsf:.0f}/sqft, avg DOM {row.avg_dom:.1f}, affordability score {row.affordability:.1f}.")
