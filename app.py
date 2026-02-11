import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Interactive Data Dashboard")

# 1. File Uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Load data
    try:
        df = pd.read_csv(uploaded_file)
    except:
        df = pd.read_excel(uploaded_file)

    # 2. Sidebar Filters
    st.sidebar.header("Filter Options")
    columns = df.columns.tolist()
    selected_col = st.sidebar.selectbox("Select Column for X-axis", columns)
    
    # 3. Data Preview
    with st.expander("View Raw Data"):
        st.write(df.head())

    # 4. Simple Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Unique Values", df[selected_col].nunique())

    # 5. Dynamic Visualization
    st.subheader(f"Analysis of {selected_col}")
    fig = px.histogram(df, x=selected_col, color_discrete_sequence=['#00CC96'])
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Please upload a file to begin.")
