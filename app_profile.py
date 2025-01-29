##Build research profile 

import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Carlien Rust"
field = "Psychiatry"
institution = "University of Stellenbosch"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload list of publications", type="csv")

if uploaded_file:
  publications = pd.read_csv(uploaded_file)
  st.dataframe(publications)
  # Add filtering for year or keyword
  keyword = st.text_input("Filter by keyword", "")
  if keyword:
    #filtered = publications[publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
    filtered = publications[publications.apply(
            lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
    st.write(f"Filtered Results for '{keyword}':")
    st.dataframe(filtered)
  else:
    st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
  if "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)
  else:
    st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "17524296@sun.ac.za"
st.write(f"You can reach {name} at {email}.")
