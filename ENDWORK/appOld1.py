import streamlit as st
from db import add_user, update_user, remove_user
from scheduler import start_scheduler

start_scheduler()

st.title("☁️ Clothing Advisor")

mode = st.selectbox("Select mode", ["Subscribe", "Update Info", "Unsubscribe"])

if mode == "Subscribe":
    email = st.text_input("Email")
    phone = st.text_input("Phone (optional)")
    latitude = st.number_input("Latitude", value=40.0)
    longitude = st.number_input("Longitude", value=-74.0)
    notification_hour = st.number_input("Notification Hour (0–23)", value=7)
    children = st.text_area("Children's ages (comma-separated)")
    notes = st.text_area("Activities / Notes (school, play, sports...)")
    contact = st.radio("Preferred Contact", ["email", "phone"])

    if st.button("Submit"):
        user = {
            "email": email,
            "phone": phone,
            "latitude": latitude,
            "longitude": longitude,
            "notification_hour": notification_hour,
            "children": [int(x.strip()) for x in children.split(",")],
            "notes": notes,
            "preferred_contact": contact
        }
        add_user(user)
        st.success("You're subscribed!")

elif mode == "Update Info":
    email = st.text_input("Enter your registered email")
    # You could build a lookup and edit interface

elif mode == "Unsubscribe":
    email = st.text_input("Enter your registered email to unsubscribe")
    if st.button("Unsubscribe"):
        # Lookup and delete
        st.success("You've been unsubscribed.")