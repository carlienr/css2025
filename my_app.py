import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "Contact"],
)

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Carlien Rust"
    field = "Psychiatry"
    institution = "University of Stellenbosch"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            #filtered = publications[publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
            filtered = publications[publications.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    name = "Dr. Carlien Rust"
    email = "17524296@sun.ac.za"
    st.write(f"You can reach {name} at {email}.")
    sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
    selected = st.feedback("thumbs")
    if selected is not None:
        st.markdown(f"You selected: {sentiment_mapping[selected]}")
