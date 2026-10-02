
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Google Play Store Analytics",
    layout="wide"
)

st.title("Google Play Store Data Analytics")
st.write("Elevance Skills | Final Internship Project")

df = pd.read_csv("googleplaystore.csv")

st.subheader("Google Play Store Dataset")
st.dataframe(df)

st.sidebar.title("Project Navigation")

project = st.sidebar.selectbox(
    "Select Project",
    [
        "Project 1 - Hexbin",
        "Project 2 - Sunburst",
        "Project 3 - Calendar Heatmap",
        "Project 4 - Streamgraph",
        "Project 5 - Clustered Heatmap",
        "Project 6 - Radar Chart"
    ]
)

st.header(project)
st.info("Project visualisation will appear here.")
