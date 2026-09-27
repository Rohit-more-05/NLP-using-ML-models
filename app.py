import streamlit as st
from models_config import get_model_names, get_model_details
import ui_components as ui

def main():
    ui.set_page_config()
    ui.apply_custom_styles()
    
    # Sidebar Navigation
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2040/2040504.png", width=100)
    st.sidebar.title("Configuration")
    st.sidebar.markdown("Select a model to view its details and accuracy.")
    
    model_names = get_model_names()
    selected_model_name = st.sidebar.radio(
        "Choose a Model Strategy:",
        model_names
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        **What is NLP?**
        Natural Language Processing (NLP) is a branch of artificial intelligence that helps computers understand, interpret and manipulate human language.
    """)
    
    # Main Content Area
    ui.render_header()
    
    # Render Selected Model Details
    if selected_model_name:
        details = get_model_details(selected_model_name)
        if details:
            ui.render_model_details(details)
            ui.render_simulation_section(selected_model_name)

if __name__ == "__main__":
    main()
