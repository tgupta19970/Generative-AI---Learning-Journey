# Task 2 - Price Calculater

# Import Streamlit Library
import streamlit as st

# Display a Title
st.title("Price Calculator App!")
# Take price number input from user
price = st.number_input("Please enter price: ")
# Create a slider to select a percentage from 0 to 50
percent_slider = st.slider("Select a percentage between 0 to 50% : ", 0, 50)
# Display a selected percetages
st.write(f"Selected percentages: {percent_slider}")
# Display a Orignal Price, Discount % and Final Price when the button is clicked
if st.button("Calculate"):

    # Check that price value should be positive
    if (price < 1):
        st.warning("Price value must be positive")
    else :

        # Calculate discounted amount
        discount_amount = (price * percent_slider) / 100
        final_price = price - discount_amount

        # Show results by using st.success()
        st.success(f"Orignal Price: {price}")
        st.success(f"Discount: {percent_slider}%")
        st.success(f"Final Price: {final_price}")

        # Extra optional show before and after values in a table by using st.table()

        data = {
            "Before": [f"{price:.2f}"],
            "After": [f"{final_price:.2f}"]
            }
        st.table(data)
