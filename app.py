import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

st.set_page_config(page_title="ARPU Pricing Co-Pilot", layout="wide")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Navigation
st.sidebar.title("🔧 Navigation")
page = st.sidebar.radio(
    "Choose a demo step:",
    [
        "🏠 Home",
        "📁 Step 1: File Intake & Parsing",
        "🧠 Step 2: AI-Powered Summarization",
        "📈 Step 3: Simulation & Optimization",
        "🧮 Step 4: Interactive Insights",
        "✅ Step 5: Decision-Ready Output"
    ]
)

# ----------------------------------
# PAGE: HOME
# ----------------------------------
if page == "🏠 Home":
    # ========== Hero Section ==========
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("logo.png", width=150)
    with col2:
        st.markdown("<h2 style='text-align:center;'>⚡ Adaptive Risk Pricing & Underwriting Engine (ARPU)</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:18px;'>The AI-Powered Pricing Co‑Pilot for Reinsurance</p>", unsafe_allow_html=True)

    st.markdown("---")

    # ========== How It Works Image ==========
    st.image("How_ARPU_Works.png", use_container_width=True)


    st.markdown("---")

    # ========== Step-by-Step Flow Icons ==========
    st.markdown("### 🧭 What You’ll Explore in This Demo")
    st.markdown("""
    **Step 1: Submission Summary**  
    Upload or preview reinsurance submission data.

    **Step 2: RL Pricing Simulation**  
    Simulate optimal structures using reinforcement learning.

    **Step 3: Portfolio What‑If**  
    Evaluate risk-return under different treaty assumptions.

    **Step 4: Chat with ARPU**  
    Ask questions and get insights from the pricing co-pilot.

    **Step 5: Final Recommendation**  
    View the best structure with explainable metrics.
    """)

    st.markdown("---")

    # ========== CTA ==========
    st.success("Use the sidebar to step through the demo.")


# ----------------------------------
# STEP 1: File Intake & Parsing
# ----------------------------------
elif page == "📁 Step 1: File Intake & Parsing":
    st.header("📁 Step 1: File Intake & Parsing")

    col1, col2 = st.columns([1, 9])
    with col1:
        st.image("step1_icon.png", width=64)
    with col2:
        st.markdown("#### Upload Your Submission File")

    st.markdown("""
    ARPU begins by **reading and parsing your submission** — just like a pricing analyst.
    
    🧾 **Supported formats:** PDF, CSV, XLSX  
    📦 Common contents:  
    • Statement of Values (SOV)  
    • Historical loss runs  
    • Cat model outputs  
    • Location-level exposures
    """)

    uploaded_file = st.file_uploader("📤 Upload your submission", type=["pdf", "csv", "xlsx"])
    use_sample = st.checkbox("Use sample submission instead", value=True)

    if uploaded_file or use_sample:
        st.success("✅ Submission loaded successfully.")
        st.markdown("🔍 Running LLM-powered parser to extract key risk insights...")

        with st.spinner("Extracting..."):
            time.sleep(2)

        st.markdown("### 📄 Submission Summary (Example)")
        st.markdown("""
        **Portfolio Snapshot:**  
        • **Total Insured Value (TIV):** `$150M`  
        • **Loss History:** 3 major events over 5 years  
        • **PML (1‑in‑100):** `$60M`  
        • **Region:** US Southeast — 🌀 Hurricane-prone  
        
        These features will inform pricing simulations and scenario modeling.
        """)

        # Simulated preview DataFrame
        preview_df = pd.DataFrame({
            "Property_ID": [101, 102, 103, 104],
            "State": ["FL", "TX", "LA", "FL"],
            "TIV ($)": [2_000_000, 1_500_000, 3_250_000, 1_800_000],
            "Peril": ["Wind", "Flood", "All Other", "Wind"],
            "Historical_Loss ($)": [250_000, 0, 180_000, 75_000],
            "Cat_PML_100yr ($)": [600_000, 400_000, 900_000, 500_000]
        })

        with st.expander("🔽 View Raw Parsed Table"):
            st.dataframe(preview_df, use_container_width=True)

        st.info("➡️ Continue to **Step 2** to summarize and simulate pricing.")
    else:
        st.warning("📂 Upload a file or use the sample to proceed.")


# ----------------------------------
# STEP 2: AI Summarization
# ----------------------------------
elif page == "🧠 Step 2: AI-Powered Summarization":
    st.header("Step 2: AI-Powered Summarization")
    st.image("step2_icon.png", width=100)

    st.markdown("""
    ### 🔍 Submission Intelligence with AI  
    ARPU uses a fine-tuned Large Language Model (LLM) to read the raw submission (PDFs, XLSX, CSV) and instantly extract key attributes for underwriting analysis.
    
    This includes:
    - **Exposure Signals:** TIV, CAT model outputs, regional hazards  
    - **Loss Experience:** Event years, incurred losses, trend lines  
    - **Structural Risk Ratios:** PML/AAL vs TIV, year-over-year volatility  
    - **Narrative Clues:** Notes on exclusions, coverage gaps, and data anomalies

    ⏱️ What normally takes hours of manual parsing is done in seconds, giving underwriters a clean view of risk for triage and modeling.
    """)

    st.markdown("#### 🧾 AI-Generated Submission Summary")
    
    summary = {
        "Total Insured Value (TIV)": "$150M",
        "Average Annual Loss (AAL)": "$8.2M",
        "Probable Max Loss (PML, 1-in-100)": "$60M",
        "Loss Events": "3 major CAT losses: 2018, 2021, 2023",
        "Hazard Region": "US Southeast — High CAT exposure (hurricanes)",
        "Construction Quality": "Mixed, mostly frame — ↑ Vulnerability",
        "Occupancy Type": "Residential + Light Commercial mix",
        "CAT Model Score": "6.8 / 10 — moderately exposed",
        "PML / TIV Ratio": "40% — indicates concentration risk",
        "Coverage Notes": "Limited flood exclusion; high deductible layer"
    }

    df_summary = pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])
    st.table(df_summary)

    st.info("✅ AI summarization complete. You can now proceed to RL pricing simulation in Step 3.")


# ----------------------------------
# STEP 3: Simulation & Optimization
# ----------------------------------
elif page == "📈 Step 3: Simulation & Optimization":
    st.header("Step 3: RL‑Driven Pricing Simulation")
    st.image("step3_icon.png", width=100)
    st.markdown("""
    In this step, an RL agent explores different pricing structures to identify high-performing combinations of:
    - **Retention**
    - **Limit**
    - **Rate-on-Line (ROL)**

    The output is a landscape of trade-offs between **profit**, **expected loss**, and **CVaR**.
    """)

    # Simulate pricing output
    def simulate_pricing():
        data = {
            "Retention ($M)": [20, 50, 100],
            "Limit ($M)": [100, 200, 300],
            "ROL (%)": [12.5, 10.8, 9.5],
            "Expected Loss ($M)": [8.1, 7.2, 6.8],
            "CVaR_99 ($M)": [25.0, 22.5, 21.1],
            "ROI (%)": [18.2, 20.5, 22.3]
        }
        return pd.DataFrame(data)

    df = simulate_pricing()
    st.markdown("### 📊 Candidate Pricing Structures")
    st.dataframe(df, use_container_width=True)

# ----------------------------------
# STEP 4: Interactive Insights
# ----------------------------------
elif page == "🧮 Step 4: Interactive Insights":
    st.header("Step 4: Portfolio What‑If Analysis")
    st.image("step4_icon.png", width=100)
    st.markdown("""
    Adjust retention, limit, or catastrophe scenario to simulate the portfolio impact in real time.
    
    Common use cases:
    * Test response to 1-in-250 cat events  
    * Adjust treaty layers for margin or tail risk  
    * Preview how pricing shifts affect ROI  
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        retention = st.slider("Retention ($M)", 10, 200, 50, step=10)
    with col2:
        limit = st.slider("Limit ($M)", 50, 500, 200, step=50)
    with col3:
        cat_scenario = st.selectbox("Catastrophe Scenario", [
            "Baseline (1-in-100)", "Moderate (1-in-150)", "Extreme (1-in-250)"
        ])

    st.markdown(f"**Scenario:** Retention = {retention}M | Limit = {limit}M | Scenario = {cat_scenario}")

    if st.button("Simulate Impact"):
        st.success("✅ Scenario simulated.")
        result = {
            "Expected Loss": "$7.8M",
            "CVaR_99": "$21.6M",
            "ROI": "23.1%"
        }
        st.table(pd.DataFrame.from_dict(result, orient="index", columns=["Value"]))

# ----------------------------------
# STEP 5: Decision-Ready Output
# ----------------------------------
elif page == "✅ Step 5: Decision-Ready Output":
    st.header("Step 5: Decision-Ready Output")
    st.image("step5_icon.png", width=100)
    st.markdown("""
    After simulation and scenario testing, ARPU generates a final, exportable pricing recommendation:
    
    ✅ Transparent  
    ✅ Clause-aware  
    ✅ Aligned with portfolio objectives  
    """)

    recommendation = {
        "Recommended Retention": "$50M",
        "Limit": "$200M",
        "ROL": "10.8%",
        "Expected Loss": "$7.2M",
        "CVaR (99%)": "$22.5M",
        "ROI": "20.5%",
        "Notes": "Balanced structure with acceptable tail risk and margin"
    }
    st.markdown("### 📄 Final Recommendation")
    st.table(pd.DataFrame.from_dict(recommendation, orient="index", columns=["Value"]))

    if st.button("Download PDF"):
        st.success("📥 Your quote packet will be sent to your inbox.")

