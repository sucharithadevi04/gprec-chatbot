import streamlit as st
import json

def show_contact():
    st.subheader("📞 Contact Details")
    
    # Try to load faculty data
    try:
        with open("data/faculty_data.json", "r") as f:
            faculty_data = json.load(f)
    except FileNotFoundError:
        st.error("Faculty data file not found!")
        return
    
    # Get unique department list
    departments = sorted(set(f.get("department", "Unknown") for f in faculty_data))
    selected_dept = st.selectbox("Select Department", departments)
    
    # Filter faculty by department
    dept_faculty = [f for f in faculty_data if f.get("department") == selected_dept]
    
    # Search functionality
    search_query = st.text_input("Search faculty by name")
    if search_query:
        search_query_lower = search_query.lower()
        dept_faculty = [
            f for f in dept_faculty
            if search_query_lower in (f.get("name") or f.get("Name of the faculty", "")).lower()
        ]
    
    # Display faculty information
    if dept_faculty:
        for f in dept_faculty:
            faculty_name = f.get("name") or f.get("Name of the faculty", "Unknown")
            with st.expander(faculty_name):
                st.write(f"**Designation:** {f.get('designation') or f.get('Designation', 'N/A')}")
                st.write(f"**Qualifications:** {f.get('qualifications') or f.get('Qualifications', 'N/A')}")
                st.write(f"**Research Interests:** {f.get('research_interest') or f.get('Research Interest', 'N/A')}")
                if f.get("google_scholar") or f.get("Google Scholar"):
                    st.markdown(f"[Google Scholar]({f.get('google_scholar') or f.get('Google Scholar')})")
                if f.get("vidwan_profile") or f.get("Vidwan Profile"):
                    st.markdown(f"[Vidwan Profile]({f.get('vidwan_profile') or f.get('Vidwan Profile')})")
                if f.get("apaar_id") or f.get("APAAR ID"):
                    st.write(f"**APAAR ID:** {f.get('apaar_id') or f.get('APAAR ID')}")
    else:
        st.warning("No matching faculty found.")
