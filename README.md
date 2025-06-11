# 💊 Drugs, Side Effects and Medical Condition  (  ML _ FA _ DA projects )

An interactive, real-time **Drug Analytics Dashboard** built using **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**. This project analyzes drug reviews, ratings, side effects, and medical conditions with **live news integration** to create an engaging user experience. Perfect for healthcare professionals, data scientists, and medical researchers.

---

## 📌 Features

- 🔎 **Drug Search** with summary, ratings, and medical condition info
- 📊 **Charts**: Ratings, reviews, conditions, and side effects
- 🧠 **Top 100 Drugs**: Sidebar listing popular drugs
- 📰 **Live Drug News**: Real-time medical news & FDA alerts via RSS
- 🌐 **External Links**: Drug info & condition pages included
- 🎨 Beautifully themed layout with animation (Lottie)

---

## 🏗️ Project Architecture

```bash
DrugsDashboardProject/
│
├── dashboard/              # Streamlit dashboard app
│   └── app.py              # Main Streamlit application
│
├── data/                   # Raw and cleaned dataset files
│   ├── drugs_side_effects_drugs_com.csv
│   └── cleaned_drugs_dashboard.csv
│
├── notebooks/             # Jupyter notebooks for preprocessing/EDA
│   └── eda_analysis.ipynb
│
├── src/                   # Utility or modular Python files (future use)
│
├── assets/                # Images, icons, animations
│   └── top_drugs.png
│
├── requirements.txt       # Python package dependencies
└── README.md              # 📄 Project documentation
```

---

## 🧪 Dataset Overview

The dataset includes detailed drug information from [Drugs.com](https://www.drugs.com/):

| Column | Description |
|--------|-------------|
| `drug_name` | Name of the drug |
| `generic_name` | Generic name |
| `brand_names` | Commercial brand names |
| `medical_condition` | Target condition |
| `medical_condition_url` | 🔗 Condition link |
| `drug_classes` | Drug category (e.g., Antibiotic) |
| `activity` | Effectiveness (%) |
| `rx_otc` | Prescription or OTC |
| `pregnancy_category` | Risk for pregnancy |
| `csa` | Controlled Substance Schedule |
| `alcohol` | Interaction level |
| `side_effects` | Common effects |
| `no_of_reviews` | Review count |
| `rating` | Average user rating |
| `drug_link` | 🔗 External drug URL |

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the app
```bash
streamlit run dashboard/app.py
```

---

## 📸 Screenshots

| Feature | Preview |
|--------|---------|
| 💡 Dashboard Home | ![home](assets/drugs.png) |
| 📊 Charts | Ratings & Reviews | 
| 📰 News | FDA + WebMD Live News |

---

## 📬 Future Enhancements
- ✅ Real-time search auto-suggestions
- ✅ Drug comparison tool
- ✅ Dark mode toggle
- ✅ ML-based side effect prediction

---

## 🧑‍💻 Developed By
**Jaykumar Girase**  
Intern @ Unified Mentor Pvt Ltd  
Mentor-Guided Analytics Internship  

---

## 📄 License
This project is open for educational and non-commercial use under MIT License.

---

> "Know more. Be sure." — Inspired by [Drugs.com](https://www.drugs.com/)
