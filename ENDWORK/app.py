import streamlit as st
from datetime import time
from streamlit_folium import st_folium
import folium
from datetime import datetime
import pytz
from llm import get_clothing_advice
from weather import get_weather

st.set_page_config(page_title="Clothing Advisor", layout="centered")

st.title("👕 Weather-based Clothing Advisor Subscription")

# ---------------------------
# 1. Select contact method
# ---------------------------
contact_method = st.radio("Preferred Contact Method", ["Email", "Phone"])
if contact_method == "Email":
    email = st.text_input("Your Email")
    phone = None
else:
    phone = st.text_input("Your Phone Number")
    email = None

# ---------------------------
# 2. Interactive Map for Location
# ---------------------------
st.subheader("📍 Select Your Location")

# Kaunas, Lithuania coordinates
lat, lon = 54.8985, 23.9036
KAUNAS_LOCATION = [lat, lon]

# Create the folium map
map_object = folium.Map(location=KAUNAS_LOCATION, zoom_start=13)

# Add a clean custom marker icon
custom_icon = folium.Icon(color="blue", icon="map-marker", prefix="fa")
folium.Marker(
    location=KAUNAS_LOCATION,
    draggable=True,
    icon=custom_icon
).add_to(map_object)

# Display map (in tight container)
map_result = st_folium(
    map_object,
    height=350,
    returned_objects=["last_marker_drag"],
    use_container_width=True
)

# ABSOLUTE MINIMAL vertical spacing
st.markdown(
    """
    <style>
    .element-container:has(.folium-map) + div {
        margin-top: -40px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Read map coordinates
if map_result and map_result.get("last_marker_drag"):
    lat = map_result["last_marker_drag"]["lat"]
    lon = map_result["last_marker_drag"]["lng"]
    st.info(f"📍 Latitude: {lat:.4f}, Longitude: {lon:.4f}")
else:
    st.warning("👈 Drag the marker to your location.", icon="📌")

# Extra spacing reduction below the warning/info
st.markdown("<div style='margin-bottom: -2rem;'></div>", unsafe_allow_html=True)

# ---------------------------
# 3. Time Picker
# ---------------------------
st.subheader("⏰ Notification Time")
notif_time = st.time_input("When should we send your clothing advice?", value=time(7, 0))

# ---------------------------
# 4. Add Children Info
# ---------------------------

st.subheader("🙋 Your Info")
gender = st.radio("Your Gender", ["Male", "Female"])

st.subheader("🧒 Children Info")

# Initialize children list in session state
if "children" not in st.session_state:
    st.session_state.children = []

# Add new child
if st.button("➕ Add a child"):
    st.session_state.children.append({
        "name": "",
        "birthdate": datetime(2018, 1, 1),
        "gender": "Male",
        "notes": ""
    })

# Render each child
updated_children = []
for i, child in enumerate(st.session_state.children):
    st.markdown(f"---\n**Child #{i+1}**")

    col1, col2, col3 = st.columns([1.2, 1.2, 0.6])
    name = col1.text_input("Name", value=child.get("name", ""), key=f"name_{i}")
    birthdate = col2.date_input(
        "Birth Month (select 1st of month)",
        value=child.get("birthdate", datetime(2018, 1, 1)),
        key=f"birthdate_{i}"
    )
    remove = col3.button("❌ Remove", key=f"remove_{i}")

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"],
        index=["Male", "Female", "Other"].index(child.get("gender", "Male")),
        key=f"gender_{i}",
        horizontal=True
    )

    notes = st.text_input(
        "Notes (school, activities, etc.)",
        value=child.get("notes", ""),
        key=f"notes_{i}"
    )

    # Only add to updated list if NOT removed
    if not remove:
        updated_children.append({
            "name": name,
            "birthdate": birthdate,
            "gender": gender,
            "notes": notes
        })

# Update session state
st.session_state.children = updated_children

# ---------------------------
# 5. Additional Notes
# ---------------------------
notes = st.text_area("📝 Any other notes or preferences?")

# ---------------------------
# 6. Submit
# ---------------------------
if st.button("✅ Subscribe"):
    if (email or phone) and lat and lon:
        st.success("✅ Subscription saved! You will receive your clothing advice at your selected time.")
        st.json({
            "email": email,
            "phone": phone,
            "lat": lat,
            "lon": lon,
            "time": notif_time.strftime("%H:%M"),
            "children": updated_children,
            "notes": notes
        })
        # Call your db.add_user(...) function here
    else:
        st.error("❌ Please complete all required fields including map location.")

# ---------------------------
# 6. Try it now
# ---------------------------
st.markdown("## 🚀 Try It Now Without Subscribing")

if st.button("🧪 Get Clothing Recommendation Now"):
    if lat is None or lon is None:
        st.error("Please select a location on the map first.")
    else:
        st.info("Fetching weather and generating clothing recommendation...")

        # Fetch weather
        weather = get_weather(lat, lon)

        # Prepare simple prompt
        prompt = f"""
        Weather: {weather}
        User gender: {gender}
        Children: {[
            {'name': c['name'], 'gender': c['gender'], 'birthdate': c['birthdate'].strftime('%Y-%m')}
            for c in st.session_state.children
        ]}
        Notes: {notes}
        Please recommend clothing for going outdoors now.
        """

        # Run prompt through your LLM
        recommendation = get_clothing_advice(prompt)

        # Display result
        st.success("👕 Clothing Recommendation:")
        st.markdown(f"**{recommendation}**")