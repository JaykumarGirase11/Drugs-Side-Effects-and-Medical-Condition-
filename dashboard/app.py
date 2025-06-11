import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests
import feedparser

# Set Streamlit config
st.set_page_config(page_title="Drugs Dashboard", layout="wide")

# Load data
df = pd.read_csv('data/cleaned_drugs_dashboard.csv')

# Lottie animation loader
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Working animation
drug_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dy6cniia.json")

# ================= CUSTOM STYLING =================
st.markdown("""
    <style>
    html, body, .main {
        background-color: #f5f7fa;
    }
    h1 {
        font-family: 'Segoe UI', sans-serif;
        font-size: 2.8rem;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .title-sub {
        text-align: center;
        color: #6b7280;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .hero {
        background: linear-gradient(120deg, #2563eb, #3b82f6);
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .block-title {
        background: linear-gradient(to right, #4f46e5, #3b82f6);
        color: white;
        padding: 0.6rem 1.5rem;
        border-radius: 12px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-top: 2rem;
        margin-bottom: 1rem;
        display: inline-block;
    }
    .stDataFrame {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        background-color: white;
        padding: 0.5rem;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin: 10px 0;
    }
    .card h3 {
        color: #2563eb;
        margin-bottom: 0.2rem;
    }
    .video-card {
        padding: 1rem;
        border-radius: 10px;
        background-color: white;
        margin-bottom: 1rem;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
from PIL import Image

# Load image
image = Image.open("assets/drugs.png")

# ✅ Only center the image (not the title or list)
st.sidebar.markdown(
    "<div style='display: flex; justify-content: center;'>",
    unsafe_allow_html=True
)
st.sidebar.image(image, width=400)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Title stays normal
st.sidebar.title("Top 100 Drugs")

# Drug list
top_100 = df['drug_name'].value_counts().head(100).index.tolist()
st.sidebar.markdown("\n".join([f"- {drug}" for drug in top_100]))
st.sidebar.markdown("---")




# ================= HERO SECTION =================
st.markdown("""
    <div class="hero">
        <h1>💊 Welcome to Drug Analytics Portal</h1>
        <p style='font-size: 1.1rem;'>Get insights on drug reviews, ratings, side effects, FDA approvals, medical news and more</p>
    </div>
""", unsafe_allow_html=True)
if drug_animation:
    st_lottie(drug_animation, height=250)

# ================= SEARCH =================
st.markdown("<div class='block-title'>🔎 Search for a Drug</div>", unsafe_allow_html=True)
search = st.text_input("Type a drug name or condition")
if search:
    filtered = df[df['drug_name'].str.contains(search, case=False) | df['medical_condition'].str.contains(search, case=False)]

    for _, row in filtered.iterrows():
        drug_name = row.get('drug_name', 'N/A')
        generic = row.get('generic_name', 'N/A')
        condition = row.get('medical_condition', 'N/A')
        csa = row.get('csa', 'N/A')

        # ✅ Only show links if they are valid
        drug_link = row.get('drug_link', '')
        med_link = row.get('medical_condition_url', '')

        drug_link_html = f"<p><a href='{drug_link}' target='_blank'>🔗 Drug Info</a></p>" if isinstance(drug_link, str) and drug_link.startswith('http') else ""
        condition_link_html = f"<p><a href='{med_link}' target='_blank'>🌐 Condition Info</a></p>" if isinstance(med_link, str) and med_link.startswith('http') else ""

        st.markdown(f"""
            <div class='card'>
                <h3>💊 {drug_name}</h3>
                <p><b>Generic Name:</b> {generic}</p>
                <p><b>Medical Condition:</b> {condition}</p>
                <p><b>CSA Schedule:</b> {csa}</p>
                {drug_link_html}
                {condition_link_html}
            </div>
        """, unsafe_allow_html=True)


# ================= NAVIGATION =================
section = st.selectbox("📂 Go to Section", [
    "📄 Dataset Overview",
    "⭐ Ratings Overview",
    "💊 Top Reviewed Drugs",
    "⚠️ Common Side Effects",
    "🩺 Frequent Medical Conditions",
])

# ================= SECTION VIEWS =================
if section == "📄 Dataset Overview":
    st.markdown("<div class='block-title'>📄 Full Dataset</div>", unsafe_allow_html=True)
    st.dataframe(df)

elif section == "⭐ Ratings Overview":
    st.markdown("<div class='block-title'>⭐ Rating Distribution</div>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df['rating'], bins=10, kde=True, color='skyblue', ax=ax)
    st.pyplot(fig)

elif section == "💊 Top Reviewed Drugs":
    st.markdown("<div class='block-title'>💊 Most Reviewed Drugs</div>", unsafe_allow_html=True)
    top_reviews = df.groupby('drug_name')['no_of_reviews'].sum().sort_values(ascending=False).head(5)
    for name in top_reviews.index:
        sidefx = df[df['drug_name'] == name]['side_effects'].values[0][:150]
        st.markdown(f"<div class='card'><h3>💊 {name}</h3><p>{sidefx}...</p></div>", unsafe_allow_html=True)

elif section == "⚠️ Common Side Effects":
    st.markdown("<div class='block-title'>⚠️ Top 10 Side Effects</div>", unsafe_allow_html=True)
    side_effect_series = df['side_effects'].str.split(';').explode().str.strip()
    top_side_effects = side_effect_series.value_counts().head(10)
    fig_se, ax_se = plt.subplots()
    sns.barplot(x=top_side_effects.values, y=top_side_effects.index, palette='coolwarm', ax=ax_se)
    ax_se.set_title("Most Reported Side Effects")
    st.pyplot(fig_se)

elif section == "🩺 Frequent Medical Conditions":
    st.markdown("<div class='block-title'>🩺 Top Medical Conditions</div>", unsafe_allow_html=True)
    top_conditions = df['medical_condition'].value_counts().head(10)
    fig_cond, ax_cond = plt.subplots()
    sns.barplot(x=top_conditions.values, y=top_conditions.index, palette='magma', ax=ax_cond)
    ax_cond.set_title("Most Treated Conditions")
    st.pyplot(fig_cond)




# ================= FOOTER =================
st.markdown("""
    <hr style='margin-top: 3rem;' />
    <center style='color: #6b7280;'> Built by <b>Jaykumar Girase ❤</b> · 💼Unified Mentor Internship · Powered by Python & Streamlit</center>
""", unsafe_allow_html=True)
