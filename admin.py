import datetime
import pandas as pd
import streamlit as st

# Global DataFrame to store parking lot data
parking_lot = pd.DataFrame(columns=['Registration_no', 'Owner_name', 'Email', 'Date_of_allocation', 'Slot'])

# Function to add a new vehicle to the Parking Lot
def add_vehicle(reg_no, owner_name, email, d_o_a, slot):
    global parking_lot
    new_vehicle = pd.DataFrame({'Registration_no': [reg_no],
                                 'Owner_name': [owner_name],
                                 'Email': [email],
                                 'Date_of_allocation': [d_o_a],
                                 'Slot': [slot]})
    parking_lot = parking_lot.append(new_vehicle, ignore_index=True)

# Function to sort the Parking Lot by a particular column
def sort_by(column):
    global parking_lot
    parking_lot = parking_lot.sort_values(column)

# Function to search for vehicles in the Parking Lot
def search_vehicle(search_term):
    global parking_lot
    return parking_lot[parking_lot.astype(str).apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)]

# Streamlit app layout
def app():
    st.set_page_config(page_title="Smart-Parking System")
    st.title("Smart-Parking System")
    st.write("Parking Lot - Register and Get your Parking Slot.")

    # Add new vehicle form
    st.header("Add new vehicle")
    reg_no = st.text_input("Registration no", key="reg_no")
    owner_name = st.text_input("Owner name", key="owner_name")
    email = st.text_input("Email", key="email")
    d_o_a = st.date_input("Date of allocation", key="d_o_a", value=datetime.date.today())
    slot = st.number_input("Slot number", key="slot", min_value=1, max_value=10)
    add_button = st.button("Add", key="add_button")
    if add_button:
        add_vehicle(reg_no, owner_name, email, d_o_a, slot)
        st.success("Vehicle added successfully!")

  

    # Show all vehicles in the Parking Lot
    st.header("All vehicles in Parking Lot")
    sort_column = st.selectbox("Sort by", options=parking_lot.columns, key="sort_column")
    sort_button = st.button("Sort", key="sort_button")
    if sort_button:
        sort_by(sort_column)
    if not parking_lot.empty:
        st.table(parking_lot)
    else:
        st.warning("Parking lot is empty")

if __name__ == '__main__':
    app()
