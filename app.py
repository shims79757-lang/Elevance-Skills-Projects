
import streamlit as st
import pandas as pd

# Dashboard configuration
st.set_page_config(
    page_title="Google Play Store Analytics",
    page_icon="📊",
    layout="wide"
)

# GitHub repository
REPO = (
    "https://github.com/"
    "shims79757-lang/Elevance-Skills-Projects"
)

# Dashboard title
st.title("Google Play Store Data Analytics")
st.caption("Elevance Skills | Python Internship Final Project")

st.markdown("---")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("googleplaystore.csv")

try:
    df = load_data()
except Exception as error:
    st.error(f"Dataset loading error: {error}")
    st.stop()

# Sidebar navigation
st.sidebar.header("Project Navigation")

projects = {
    "Home": None,

    "Project 1 - Hexbin Analysis":
        "Google_Play_Store_App_Analysis.ipynb",

    "Project 2 - Sunburst Chart":
        "Hierarchical_App_Market_Visualization_Project.ipynb",

    "Project 3 - Calendar Heatmap":
        "Interactive_App_Category_Heatmap_Project.ipynb",

    "Project 4 - Streamgraph":
        "App_Category_Performance_Streamgraph_Project.ipynb",

    "Project 5 - Clustered Heatmap":
        "App_Category_Performance_Analysis_Project.ipynb",

    "Project 6 - Radar Chart":
        "Comparative_App_Performance_Analysis_Project.ipynb"
}

selection = st.sidebar.radio(
    "Select a project",
    list(projects.keys())
)

# Home page
if selection == "Home":

    st.header("Project Overview")

    st.write(
        "An interactive analytics project examining "
        "Google Play Store application performance "
        "using Python and data visualisation."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Applications", len(df))

    if "Category" in df.columns:
        col2.metric(
            "App Categories",
            df["Category"].nunique()
        )

    col3.metric("Projects Completed", 6)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Available Projects")

    for project in list(projects.keys())[1:]:
        st.write("•", project)

# Individual project pages
else:

    st.header(selection)

    st.write(
        "Access the original Python notebook "
        "for the complete analysis and visualisation."
    )

    filename = projects[selection]

    # Match the notebook name in GitHub
    notebook_url = f"{REPO}/blob/main/{filename}"

    st.link_button(
        "View Project Notebook on GitHub",
        notebook_url
    )

    st.subheader("Google Play Store Dataset")

    st.dataframe(
        df.head(15),
        use_container_width=True
    )

st.markdown("---")
st.caption("Developed by Himani | Elevance Skills")
