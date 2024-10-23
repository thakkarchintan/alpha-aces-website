import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Alpha Aces Advisory", page_icon=":chart_with_upwards_trend:", layout="centered")

# Main title
st.title("Alpha Aces Advisory")
st.subheader("Global Quantitative Research & Trading")

# Create a tab for the About Us section only
tabs = st.tabs(["About Us"])

# About Us Section
with tabs[0]:
    st.header("About Us")
    st.write("""
        **Alpha Aces Advisory** is a technology-driven global quantitative research and trading firm. 
        We specialize in utilizing advanced data analytics, algorithms, and cutting-edge technology 
        to identify market inefficiencies and deliver high-quality trading strategies. 
        
        Our expertise lies in leveraging innovative tools to provide clients with tailored solutions 
        that help them navigate financial markets effectively and profitably.
        
        For any information or enquiry, contact us on alpha.acesllp@gmail.com
    """)

# Footer
st.markdown("---")
st.write("© 2024 Alpha Aces Advisory. All rights reserved.")
