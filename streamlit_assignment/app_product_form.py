# Task 3 - Product Form

# Import Streamlit Library
import streamlit as st

# Display Title
st.title("Product Form")
st.write("### Product Details")

# Initialize products list
if "products" not in st.session_state:
    st.session_state.products = []

# Sidebar
st.sidebar.header("Enter Product Details")

# Take user input for product name
product_name = st.sidebar.text_input("Product Name")

# Create a category selection dropdown with 5 category by using st.sidebar.selectbox()
category = st.sidebar.selectbox(
    "Category",
    ["Select", "Electronics", "Clothing", "Food", "Furniture", "Other"]
)

# Take user price input
price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    format="%.2f"
)

# Create a Add Product and handle button clicked
if st.sidebar.button("Add Product"):

   

    # Check product name
    if product_name == "":
        st.sidebar.warning("Please enter product name")

    # Check category
    elif category == "Select":
        st.sidebar.warning("Please select category")

    # Check that price value should be positive
    elif price < 1:
        st.sidebar.warning("Price value must be positive")
    else :
        st.sidebar.success("Product Added Successfully")
        # Show Product details in table by using st.table()
        data = {
            "Product Name": product_name,
            "Category": category,
            "Price": f"{price:.2f}"
        }

        
        st.table(data)

        
      



    
    

