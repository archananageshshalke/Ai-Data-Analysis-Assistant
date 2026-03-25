import pandas as pd
import streamlit as st

# Page config (makes it look professional)
st.set_page_config(page_title="AI Data Analyst Assistant", layout="wide")

# Title
st.title("🤖 AI Data Analyst Assistant")
st.markdown("Ask questions about the dataset and get insights instantly.")

# Load dataset
df = pd.read_csv("dataset.csv")

# Handle missing values
df = df.fillna("Unknown")

# Sidebar (professional touch)
st.sidebar.header("📌 Project Info")
st.sidebar.markdown("""
*Project:* AI Data Analyst Assistant  
*Tech:* Python, Pandas, Streamlit  
*Features:*
- Query-based analysis  
- Automated insights  
- Data visualization  
""")

# Show raw data option
if st.checkbox("Show raw data"):
    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

# User input
question = st.text_input("🔍 Ask your data question:")

# Output section
if question:
    question = question.lower()

    st.markdown("---")

    # Highest fare
    if "highest fare" in question:
        result = df.loc[df['Fare'].astype(float).idxmax()]

        st.subheader("📊 Top Passenger Analysis")
        st.write(result)

        st.success("Passengers paying higher fares were likely premium class, showing strong socio-economic segmentation.")

    # Survival analysis
    elif "survival" in question:
        st.subheader("📊 Survival Analysis")

        survival_rate = df.groupby('Sex')['Survived'].mean()
        st.write(survival_rate)

        st.bar_chart(df['Survived'].value_counts())

        st.success("Female passengers had significantly higher survival rates due to priority rescue policies.")

    # Age analysis
    elif "age" in question:
        st.subheader("📊 Age Distribution")

        st.write(df['Age'].describe())

        st.line_chart(df['Age'])

        st.success("Most passengers were adults, which influenced survival trends.")

    # Automated insights
    elif "insights" in question:
        st.subheader("📊 Automated Insights")

        st.write("1. Female survival rate is higher than male.")
        st.write("2. Higher fare passengers belong to upper class.")
        st.write("3. Age impacts survival probability.")

        st.bar_chart(df['Pclass'].value_counts())

        st.success("These patterns reflect real-world socio-economic and behavioral trends.")

    # Default
    else:
        st.warning("Try: highest fare, survival, age, insights")

# Footer (final professional touch)
st.markdown("---")
st.markdown("🚀 Built by Data Analyst | Streamlit Project")