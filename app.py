import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data
df = pd.read_csv("data/customer_segments.csv")

# Title
st.title("📊 Customer Segmentation Dashboard")
st.markdown(
    "Interactive analysis of customer demographics, income, "
    "spending behavior, and customer segments."
)

# KPI metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(df)
)

col2.metric(
    "Average Age",
    round(df["Age"].mean(), 2)
)

col3.metric(
    "Average Income",
    f"{df['Annual_Income'].mean():.2f} k$"
)

col4.metric(
    "Average Spending",
    round(df["Spending_Score"].mean(), 2)
)

st.divider()

# Segment distribution
st.subheader("Customer Segment Distribution")

segment_counts = (
    df["Segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = ["Segment", "Customer_Count"]

fig = px.bar(
    segment_counts,
    x="Segment",
    y="Customer_Count",
    title="Number of Customers in Each Segment",
    text="Customer_Count"
)

fig.update_layout(
    xaxis_title="Customer Segment",
    yaxis_title="Number of Customers"
)

st.plotly_chart(fig, use_container_width=True)

# Income vs Spending Score
st.subheader("Annual Income vs Spending Score")

fig_scatter = px.scatter(
    df,
    x="Annual_Income",
    y="Spending_Score",
    color="Segment",
    hover_data=["CustomerID", "Age", "Gender"],
    title="Customer Segments by Income and Spending",
    labels={
        "Annual_Income": "Annual Income (k$)",
        "Spending_Score": "Spending Score (1-100)"
    }
)

st.plotly_chart(fig_scatter, use_container_width=True)

# Segment Filter
st.subheader("Explore Customer Segments")

selected_segment = st.selectbox(
    "Select a Customer Segment",
    ["All Segments"] + sorted(df["Segment"].unique().tolist())
)

if selected_segment == "All Segments":
    filtered_df = df
else:
    filtered_df = df[df["Segment"] == selected_segment]

st.write(f"Customers in selected segment: **{len(filtered_df)}**")

# Selected Segment Summary

if selected_segment != "All Segments":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        len(filtered_df)
    )

    col2.metric(
        "Average Age",
        round(filtered_df["Age"].mean(), 2)
    )

    col3.metric(
        "Average Income",
        f"{filtered_df['Annual_Income'].mean():.2f} k$"
    )

    col4.metric(
        "Average Spending",
        round(filtered_df["Spending_Score"].mean(), 2)
    )

    # Customer Data
st.subheader("Customer Details")

st.dataframe(
    filtered_df[
        [
            "CustomerID",
            "Gender",
            "Age",
            "Annual_Income",
            "Spending_Score",
            "Cluster",
            "Segment"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

# Business Insights
st.divider()

st.subheader("💡 Business Insights")

st.markdown("""
### Key Customer Segment Insights

**1. High-Value Customers**
- High income and high spending behavior.
- Should be prioritized with VIP programs, premium services, and exclusive offers.

**2. High-Income Low-Spending Customers**
- Have strong purchasing capacity but relatively low spending.
- Personalized recommendations and targeted promotions can encourage higher spending.

**3. Young High-Spending Customers**
- Young customers with high spending behavior.
- Discounts, affordable bundles, and promotional campaigns can help retain them.

**4. Mature Average Customers**
- Represent the largest customer segment.
- Loyalty programs and personalized product recommendations can improve engagement.

**5. Young Average Customers**
- Young customers with moderate income and spending.
- Digital campaigns and loyalty rewards can increase engagement.

**6. Low-Income Low-Spending Customers**
- Lower income and lower spending behavior.
- Value-for-money products and budget-friendly offers are more suitable.
""")

st.subheader("📊 Average Spending Score by Segment")

segment_avg = (
    df.groupby("Segment")["Spending_Score"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig_spending = px.bar(
    segment_avg,
    x="Segment",
    y="Spending_Score",
    title="Average Spending Score by Customer Segment",
    text_auto=".2f",
    labels={
        "Segment": "Customer Segment",
        "Spending_Score": "Average Spending Score"
    }
)

st.plotly_chart(fig_spending, use_container_width=True)

st.subheader("⬇️ Download Customer Segmentation Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Segmented Customer Data",
    data=csv,
    file_name="customer_segments.csv",
    mime="text/csv"
)