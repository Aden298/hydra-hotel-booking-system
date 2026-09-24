import streamlit as st

# 1. Web Page Title & Setup
st.set_page_config(page_title="Hydra Hotel Booking", page_icon="🏨")
st.title("🏨 Hydra Hotel Booking System")
st.write("Welcome to the Hydra Hotel digital reservation portal.")
st.divider()

# 2. Interactive Web Input Fields
st.subheader("Guest Information")
name = st.text_input("Please enter your name:")
ic_number = st.text_input("Please enter your IC number:")

st.subheader("Reservation Details")
# Dropdown selection replaces text inputs to prevent user spelling errors
type_of_room = st.selectbox(
    "Select the type of room you want to book:",
    ["single", "double", "family", "suite"]
)

# Putting the numbers side-by-side using web columns
col1, col2 = st.columns(2)
with col1:
    number_of_rooms = st.number_input("Number of rooms to book:", min_value=1, value=1, step=1)
with col2:
    number_of_nights = st.number_input("Number of nights to stay:", min_value=1, value=1, step=1)

# 3. Your Original Pricing Logic
price_per_night = 0
if type_of_room == "single":
    price_per_night = 100
elif type_of_room == "double":
    price_per_night = 150
elif type_of_room == "family":
    price_per_night = 200
elif type_of_room == "suite":
    price_per_night = 300

total_cost = price_per_night * number_of_nights * number_of_rooms

st.divider()

# 4. Web Checkout & Interactive Payment processing
st.subheader("Checkout & Payment")
st.info(f"*The total cost for your stay is:* RM {total_cost:.2f}")

payment_method = st.radio("Please enter your payment method:", ["cash", "credit card"])

if payment_method == "cash":
    st.warning("⚠️ Please pay at the counter !")
    
elif payment_method == "credit card":
    card_number = st.text_input("Please enter your credit card number:", type="password")
    
    # Let the user input an amount to pay
    amount_paid = st.number_input("Please enter the amount you are paying (RM):", min_value=0.0, value=float(total_cost))
    
    # A web button to process the calculation
    if st.button("Submit Payment"):
        if amount_paid >= total_cost:
            balance = amount_paid - total_cost
            st.success("🎉 Thank you for your payment with credit card!")
            st.write(f"*Your balance is:* RM {balance:.2f}")
        else:
            st.error("❌ Insufficient amount. Please pay the total amount due.")