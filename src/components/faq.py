import streamlit as st
import json

def show_faq(data=None):
    st.subheader("❓ Frequently Asked Questions")
    
    # Try to load FAQ data
    try:
        with open("data/faq.json") as f:
            faq_data = json.load(f)
    except FileNotFoundError:
        faq_data = {}
    
    # User input
    user_question = st.text_input("Ask a question")
    
    if user_question:
        matched = False
        
        # Search in FAQ data
        for question, answer in faq_data.items():
            if user_question.lower() in question.lower():
                st.success(answer)
                matched = True
                break
        
        # Search in placement data if available
        if not matched and data is not None:
            for year in data["Year"]:
                if str(year) in user_question and "placement" in user_question.lower():
                    placement = data.loc[data["Year"] == year, "Placements"].values[0]
                    st.success(f"Placements in {year} were {placement}.")
                    matched = True
                    break
        
        # No match found
        if not matched:
            st.error("Sorry, I don't know that yet.")
