
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(page_title="AI Real Estate Market Intelligence", page_icon="🏙️", layout="wide")
DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_atlanta_housing_records.csv"
df = pd.read_csv(DATA, parse_dates=["list_date"])

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;600;800&display=swap');
.stApp {background: linear-gradient(135deg,#07111f 0%,#102a43 44%,#d4af37 160%); color: #f7fafc; font-family: Inter, sans-serif;}
.hero {padding: 2rem; border-radius: 28px; background: rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.16); box-shadow:0 25px 70px rgba(0,0,0,.35); animation: fadein 1s ease-in-out;}
.hero h1 {font-family:'Playfair Display',serif; font-size:3.2rem; margin:0; color:#fff4c2;}
.hero p {font-size:1.05rem; color:#dbeafe; max-width:950px;}
.metric-card {padding:1.2rem; border-radius:22px; background:rgba(255,255,255,.11); border:1px solid rgba(255,255,255,.18); transition: transform .25s ease, background .25s ease;}
.metric-card:hover {transform: translateY(-6px); background:rgba(255,255,255,.16);}
.metric-label {font-size:.8rem; text-transform:uppercase; color:#bfdbfe; letter-spacing:.08em;}
.metric-value {font-size:2rem; font-weight:800; color:#fff4c2;}
@keyframes fadein {from{opacity:0; transform:translateY(18px)} to{opacity:1; transform:translateY(0)}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>AI Real Estate Market Intelligence</h1>
<p>A luxury-market styled analytics command center for Metro Atlanta housing. Built to show pricing movement, affordability, inventory pressure, and location-based opportunity signals.</p>
</div>
""", unsafe_allow_html=True)

markets = st.multiselect("Choose Metro Atlanta markets", sorted(df.market.unique()), default=sorted(df.market.unique())[:6])
ptype = st.multiselect("Property type", sorted(df.property_type.unique()), default=sorted(df.property_type.unique()))
f = df[df.market.isin(markets) & df.property_type.isin(ptype)]

c1,c2,c3,c4 = st.columns(4)
metrics = [
    ("Housing Records", f"{len(f):,}"),
    ("Median Sale Price", f"${f.sale_price.median():,.0f}"),
    ("Avg Price / Sq Ft", f"${f.price_per_sqft.mean():,.0f}"),
    ("Avg Days on Market", f"{f.days_on_market.mean():.1f}"),
]
for col,(label,val) in zip([c1,c2,c3,c4], metrics):
    col.markdown(f"<div class='metric-card'><div class='metric-label'>{label}</div><div class='metric-value'>{val}</div></div>", unsafe_allow_html=True)

left,right = st.columns([1.15,.85])
with left:
    st.subheader("Market Price Benchmarking")
    market = f.groupby('market', as_index=False).agg(median_sale_price=('sale_price','median'), avg_ppsf=('price_per_sqft','mean'), avg_affordability=('affordability_score','mean'))
    chart = alt.Chart(market).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
        x=alt.X('market:N', sort='-y', title=None), y=alt.Y('median_sale_price:Q', title='Median sale price'),
        tooltip=['market','median_sale_price','avg_ppsf','avg_affordability']
    ).properties(height=360)
    st.altair_chart(chart, use_container_width=True)
with right:
    st.subheader("Inventory Risk Mix")
    risk = f.inventory_risk_segment.value_counts().reset_index()
    risk.columns=['risk','count']
    st.altair_chart(alt.Chart(risk).mark_arc(innerRadius=70).encode(theta='count:Q', color='risk:N', tooltip=['risk','count']).properties(height=360), use_container_width=True)

st.subheader("Geographic Market View")
st.map(f[['latitude','longitude']].dropna().sample(min(1200, len(f)), random_state=7))

st.subheader("AI-Generated Executive Summary")
best = market.sort_values('avg_affordability', ascending=False).head(1).iloc[0]
hot = f.inventory_risk_segment.value_counts().idxmax()
st.info(f"The strongest affordability signal is currently in {best.market}, while the dominant inventory condition across selected markets is {hot}. Pricing leadership is concentrated in higher-median-price submarkets, but days-on-market patterns reveal room for targeted negotiation and buyer opportunity.")

with st.expander("Preview source data"):
    st.dataframe(f.head(500), use_container_width=True)
