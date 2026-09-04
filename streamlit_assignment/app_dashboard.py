# Task 4 - Mini Dashboard

# Import Streamlit Library
import streamlit as st

# Display Title and Description
st.title("Simple Sales Dashboard")
st.write("A simple Sales Dashboard to track and analyze sales performance, including total sales, number of products sold, categories, prices, and key sales details in an easy-to-understand view.")

# Create a Month selection dropdown by using st.selectbox()
month = st.selectbox(
    "Month",
    ["Select", "January", "February", "March", "April"]
)

# Given a dictionary of the monthly sales
sales = {"January": 1200, "February": 1500, "March": 900, "April": 2000}


# Show month wise sales record by using st.metric()
if month != "Select":
    monthly_sales = sales[month]

    st.metric(
        label = f"{month} Sales", 
        value = f"{monthly_sales:.2f} Rs"
    )

    # Show sales records by using st.bar_chart()
    selected_sales = {
        month: monthly_sales
    }

    st.bar_chart(selected_sales)
