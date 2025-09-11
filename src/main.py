import streamlit as st
from components.home import show_home
from components.campus_map import show_campus_map
from components.faq import show_faq
from components.placements import show_placements
from components.contact import show_contact
from utils.data_loader import load_placement_data
from utils.chatbot import PlacementChatbot

st.title("🎓 College InfoBot")
st.write("Welcome to the smart assistant for students!")

# Load placement data
data = load_placement_data()
chatbot = PlacementChatbot()

# Sidebar menu
menu = st.sidebar.selectbox(
    "Choose a section",
    ["Home", "Campus Map", "FAQ", "Placements", "Placement Chatbot", "Contact"]
)

# ---------------- MENU SECTIONS ----------------
if menu == "Home":
    show_home()

elif menu == "Campus Map":
    show_campus_map()

elif menu == "FAQ":
    show_faq(data)

elif menu == "Placements":
    show_placements(data)

elif menu == "Placement Chatbot":
    st.subheader("💬 Placement NLP Chatbot")
    query = st.text_input("Ask a placement-related question")
    if query:
        st.success(chatbot.answer_question(query))

elif menu == "Contact":
    show_contact()
