import streamlit as st

background_image_url = "https://png.pngtree.com/background/20210709/original/pngtree-creative-synthesis-city-comic-real-estate-picture-image_916360.jpg"

# Set page title and icon
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏡",
)

# Load background image
background_image = "https://png.pngtree.com/background/20210709/original/pngtree-creative-synthesis-city-comic-real-estate-picture-image_916360.jpg"

# Set background image
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("{background_image}") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)



st.title("Welcome to Gurgaon Real Estate Analytics Dashboard")
st.write("This is the homepage. Choose a demo from the sidebar to explore.")

st.sidebar.success("Select the tool.")