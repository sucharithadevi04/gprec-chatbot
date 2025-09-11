import streamlit as st
import folium
from streamlit_folium import st_folium
import math

# GPREC Campus coordinates
GPREC_LAT, GPREC_LNG = 15.7742, 78.0568

# Department coordinates
DEPARTMENTS = {
    "CSE Block": [15.77375, 78.05761],
    "CSE IT": [15.77367, 78.0570],
    "Stationary": [15.773931, 78.056755],
    "ATM": [15.774008, 78.056732],
    "Girls Lounge": [15.77428, 78.05667],
    "Drawing Halls": [15.77439, 78.05658],
    "Water Plant": [15.774105, 78.056094],
    "Mechanical Block": [15.774198613972006, 78.05582202401315],
    "Civil Block": [15.773620533838598, 78.05597389604817],
    "ECE Block": [15.77361, 78.05556]
}

def calculate_distance(coord1, coord2):
    R = 6371000
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_direction(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    angle = math.degrees(math.atan2(lat2 - lat1, lon2 - lon1))
    if -45 <= angle <= 45:
        return "Go straight"
    elif 45 < angle <= 135:
        return "Turn left"
    elif -135 <= angle < -45:
        return "Turn right"
    else:
        return "Go back"

def show_campus_map():
    st.subheader("📍 GPREC Campus (Pasupula, Kurnool)")
    
    # Create map centered on GPREC
    m = folium.Map(location=[GPREC_LAT, GPREC_LNG], zoom_start=18)
    
    # Add markers for all departments
    for dept, coords in DEPARTMENTS.items():
        folium.Marker(
            coords,
            popup=dept,
            tooltip=dept,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
    
    # Navigation selectors
    from_dept = st.selectbox("Select Starting Point", list(DEPARTMENTS.keys()))
    to_dept = st.selectbox("Select Destination", list(DEPARTMENTS.keys()))
    
    # Draw route if different locations selected
    if from_dept != to_dept:
        folium.PolyLine(
            locations=[DEPARTMENTS[from_dept], DEPARTMENTS[to_dept]],
            color="red",
            weight=4,
            opacity=0.8
        ).add_to(m)
        
        # Calculate and display route information
        distance = calculate_distance(DEPARTMENTS[from_dept], DEPARTMENTS[to_dept])
        direction = get_direction(DEPARTMENTS[from_dept], DEPARTMENTS[to_dept])
        st.success(f"Route from {from_dept} to {to_dept}: {direction} for {distance:.2f} meters")
    
    # Display the map
    st_folium(m, width=700, height=500)
