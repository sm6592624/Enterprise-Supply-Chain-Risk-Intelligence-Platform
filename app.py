from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

from generate_data import generate_supply_chain_data
from sql_engine import run_sql_queries

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "supply_chain_data.csv"

st.set_page_config(page_title="Supply Chain Risk Intelligence", layout="wide")
st.title("📦 Enterprise Supply Chain Risk & Inventory Intelligence")
st.markdown("Automated analytics engine evaluating supplier delays, inventory costs, and warehouse risk profiles.")

@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        generate_supply_chain_data()
    return pd.read_csv(DATA_FILE)

try:
    df = load_data()
except FileNotFoundError:
    st.error("Dataset could not be loaded. Please try reloading the app.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Shipments", f"{len(df):,}")
col2.metric("Avg Lead Time", f"{df['lead_time_days'].mean():.1f} Days")
col3.metric("Stockout Rate", f"{(df['stockout_flag'].mean()*100):.1f}%")
col4.metric("Holding Cost", f"₹{df['inventory_holding_cost'].sum():,.2f}")

st.divider()
st.subheader("Warehouse Operational Risk Analysis (SQL Computed)")
sql_risk_df = run_sql_queries()
st.dataframe(sql_risk_df, use_container_width=True)

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Lead Time Variance by Warehouse")
    fig_box = px.box(df, x='warehouse', y='lead_time_days', color='shipment_status', points="all")
    st.plotly_chart(fig_box, use_container_width=True)

with col_right:
    st.subheader("Holding Cost Exposure by Category")
    fig_pie = px.pie(df, names='category', values='inventory_holding_cost', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)                                             