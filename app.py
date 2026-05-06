import streamlit as st
import pandas as pd
import glob

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")

# -----------------------------
# Load parquet files
# -----------------------------
def load_data(path):
    files = glob.glob(path + "/*.parquet")
    df = pd.concat([pd.read_parquet(f) for f in files])
    return df

product_df = load_data("data/gold/product_metrics")
customer_df = load_data("data/gold/customer_metrics")

# Convert date
if "order_date" in product_df.columns:
    product_df["order_date"] = pd.to_datetime(product_df["order_date"])

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Products", product_df["product_id"].nunique())

with col2:
    st.metric("Total Customers", customer_df["customer_id"].nunique())

with col3:
    st.metric("Total Revenue", int(product_df["total_revenue"].sum()))

st.divider()

# -----------------------------
# FILTERS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    category_filter = st.selectbox(
        "Category",
        ["All"] + sorted(product_df["category"].unique())
    )

with col2:
    city_filter = st.selectbox(
        "City",
        ["All"] + sorted(customer_df["city"].unique())
    )

with col3:
    search = st.text_input("🔍 Search Product")

# Apply filters
filtered_products = product_df.copy()
filtered_customers = customer_df.copy()

if category_filter != "All":
    filtered_products = filtered_products[
        filtered_products["category"] == category_filter
    ]

if city_filter != "All":
    filtered_customers = filtered_customers[
        filtered_customers["city"] == city_filter
    ]

if search:
    filtered_products = filtered_products[
        filtered_products["product_name"].str.contains(search, case=False)
    ]

# -----------------------------
# CHARTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Top Products by Revenue")
    st.bar_chart(
        filtered_products
        .sort_values("total_revenue", ascending=False)
        .head(15)
        .set_index("product_name")[["total_revenue"]]
    )

with col2:
    st.subheader("🧍 Top Customers by Revenue")
    st.bar_chart(
        filtered_customers
        .sort_values("total_revenue", ascending=False)
        .head(15)
        .set_index("customer_name")[["total_revenue"]]
    )

st.divider()

# -----------------------------
# DRILL DOWN
# -----------------------------
st.subheader("🔎 Drill Down Analysis")

col1, col2 = st.columns(2)

with col1:
    selected_product = st.selectbox(
        "Select Product",
        filtered_products["product_name"].unique()
    )

    st.write("### Product Details")
    st.dataframe(
        filtered_products[
            filtered_products["product_name"] == selected_product
        ],
        use_container_width=True
    )

with col2:
    selected_customer = st.selectbox(
        "Select Customer",
        filtered_customers["customer_name"].unique()
    )

    st.write("### Customer Details")
    st.dataframe(
        filtered_customers[
            filtered_customers["customer_name"] == selected_customer
        ],
        use_container_width=True
    )

st.divider()

# -----------------------------
# FULL DATA TABLES
# -----------------------------
st.subheader("📦 Full Product Data")

if st.checkbox("Show Product Data"):
    st.dataframe(product_df, use_container_width=True)

st.subheader("👤 Full Customer Data")

if st.checkbox("Show Customer Data"):
    st.dataframe(customer_df, use_container_width=True)