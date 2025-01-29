##Writing Python Scripts for Streamlit

import streamlit as st

st.write("Hello, Streamlit!")

##Add interactivity

#number = st.slider("Pick a number", 1, 100)

#st.write(f"You picked: {number}")

#In Streamlit, you can add headings using the st.title(), st.header(), st.subheader(), and st.markdown() functions.

#st.title("Title heading")

#st.write("Hello, Streamlit!")

#st.header("Number selection")

#number = st.slider("Pick a number", 1, 100)
#st.write(f"You picked: {number}")

##Visualise data
# My Plot of data

import pandas as pd
import plotly.express as px

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

# Display the data in the Streamlit app
st.write(data)

# Create a Plotly figure
fig = px.line(data, x="x", y="y", title="Simple Plotly Example")

# Display the plot in the Streamlit app
st.plotly_chart(fig)













