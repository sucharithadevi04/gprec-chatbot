import streamlit as st
import pandas as pd

def show_placements(data):
    st.subheader("📊 Placement Statistics")
    
    if data is not None:
        st.line_chart(data.set_index('Year'))
        if st.checkbox("Show raw data"):
            st.dataframe(data)
    else:
        st.error("Placement data file not found! Please add 'placement_data.csv' to your project folder.")
