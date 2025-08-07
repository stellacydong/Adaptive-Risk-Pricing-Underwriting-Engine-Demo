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
        st.markdown("#### Upload a Reinsurance Submission")

    st.markdown("""
    ARPU starts by **parsing the submission file**, just like a human underwriter would — extracting key attributes from raw data to prepare for analysis.

    📤 **Accepted formats:** `PDF`, `XLSX`, `CSV`  
    📦 **Expected contents:**  
    • Statement of Values (SOV)  
    • Historical Loss Runs  
    • CAT Model Outputs  
    • Location-Level Exposures  
    """)

    uploaded_file = st.file_uploader("Choose your submission file", type=["pdf", "csv", "xlsx"])
    use_sample = st.checkbox("Or use a sample submission", value=True)

    if uploaded_file or use_sample:
        st.success("✅ Submission file loaded.")
        st.markdown("🔍 **Running LLM-powered parser to extract insights...**")

        with st.spinner("Parsing submission..."):
            time.sleep(2)

        # =====================
        #   Simulated Summary
        # =====================
        st.markdown("### 📄 Submission Snapshot (Example)")
        st.markdown("""
        ARPU has extracted key attributes from your submission:

        - **Total Insured Value (TIV):** `$150M`  
        - **Loss History:** 3 major events in the past 5 years  
        - **PML (1-in-100):** `$60M`  
        - **Region:** US Southeast — 🌀 Hurricane-prone  

        These features will feed directly into pricing simulations and risk evaluation in upcoming steps.
        """)

        # Simulated parsed table preview
        preview_df = pd.DataFrame({
            "Property_ID": [101, 102, 103, 104],
            "State": ["FL", "TX", "LA", "FL"],
            "TIV ($)": [2_000_000, 1_500_000, 3_250_000, 1_800_000],
            "Peril": ["Wind", "Flood", "All Other", "Wind"],
            "Historical_Loss ($)": [250_000, 0, 180_000, 75_000],
            "Cat_PML_100yr ($)": [600_000, 400_000, 900_000, 500_000]
        })

        with st.expander("🔽 View Parsed Table"):
            st.dataframe(preview_df, use_container_width=True)

        st.success("✅ Parsing complete. Ready to analyze and simulate in Step 2.")
    else:
        st.warning("📂 Please upload a file or select the sample submission to proceed.")



# ----------------------------------
# STEP 2: AI Summarization
# ----------------------------------
elif page == "🧠 Step 2: AI-Powered Summarization":
    st.header("Step 2: AI-Powered Summarization")
    st.image("step2_icon.png", width=100)

    st.markdown("""
    ### 🔍 Intelligent Submission Parsing  
    Our AI engine ingests raw submission files (PDF, XLSX, CSV) and instantly extracts key underwriting attributes using a fine-tuned Large Language Model (LLM).  

    Within seconds, ARPU delivers a structured snapshot of submission risk — enabling faster triage, modeling, and pricing.

    **Extracted Insights Include:**
    - **📊 Exposure Metrics:** TIV, CAT model outputs, hazard zones  
    - **📉 Loss History:** Key event years, incurred losses, trend curves  
    - **⚖️ Risk Ratios:** AAL & PML vs TIV, year-over-year volatility  
    - **📝 Underwriting Clues:** Exclusions, coverage anomalies, unstructured notes
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

    st.success("✅ Submission successfully summarized. You're ready to move on to Step 3: RL-Powered Pricing Optimization.")



# ----------------------------------
# STEP 3: Simulation & Optimization
# ----------------------------------
elif page == "📈 Step 3: Simulation & Optimization":
    st.header("Step 3: RL‑Driven Pricing Simulation")
    st.image("step3_icon.png", width=100)

    st.markdown("""
    ### 🔄 Reinforcement Learning for Treaty Optimization

    In this step, ARPU uses a Reinforcement Learning (RL) agent to simulate a range of reinsurance pricing structures.  
    The agent intelligently explores combinations of:
    - **Retention** (cedent's share of risk)
    - **Limit** (maximum insurer payout)
    - **Rate-on-Line (ROL)** (premium as a % of limit)

    Each combination is scored on multiple risk-reward metrics, producing a **portfolio-efficient pricing frontier**.

    ---
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

    st.markdown("""
    ### 🧠 How to Interpret the Results

    Each row represents a **candidate structure** that balances premium income, expected loss, and tail risk:

    - **Lower Retention** transfers more risk to the reinsurer, but often comes at a higher ROL.
    - **Higher Limits** offer broader protection but increase the reinsurer’s exposure.
    - **CVaR_99** estimates the insurer’s **worst-case loss** at the 99th percentile – crucial for solvency.
    - **ROI (%)** estimates expected return, incorporating premium income and loss risk.

    ---
    
    ✅ Use this table to identify structures that align with the cedent’s **risk appetite**, **capital constraints**, and **margin goals**.

    ➡️ Proceed to **Step 4** to explore impact under different catastrophe scenarios.
    """)


# ----------------------------------
# STEP 4: Interactive Insights
# ----------------------------------
elif page == "🧮 Step 4: Interactive Insights":
    st.header("Step 4: Portfolio What‑If Analysis")
    st.image("step4_icon.png", width=100)

    st.markdown("""
    ### 🔁 Real-Time Scenario Simulation

    Use this interactive tool to **test the impact of different treaty parameters** on portfolio performance under various catastrophe scenarios.

    🔧 **You can adjust:**
    - **Retention** (cedent’s risk share)
    - **Limit** (maximum payout)
    - **Catastrophe severity** (return periods: 1-in-100, 1-in-250, etc.)

    🧪 **Common Use Cases:**
    - Stress test portfolio under extreme CAT events  
    - Analyze margin vs. tail risk trade-offs  
    - Preview impact of treaty tweaks on ROI and solvency buffer (CVaR)
    ---
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

    st.markdown(f"**🔍 Current Scenario:** Retention = `{retention}M` | Limit = `{limit}M` | Scenario = `{cat_scenario}`")

    if st.button("Simulate Impact"):
        st.success("✅ Scenario simulation complete.")

        result = {
            "Expected Loss": "$7.8M",
            "CVaR_99": "$21.6M",
            "ROI": "23.1%"
        }

        st.markdown("### 📉 Simulation Output")
        st.table(pd.DataFrame.from_dict(result, orient="index", columns=["Value"]))

        st.markdown("""
        ### 📘 How to Interpret the Results

        - **Expected Loss**: Average projected loss under the selected scenario.  
        - **CVaR_99**: Conditional Value at Risk — average loss in the worst 1% of cases. Key for regulatory and solvency planning.  
        - **ROI**: Net return after accounting for ROL and expected losses — a guide for structuring profitability.

        ---
        ✅ Use this to guide treaty negotiations, justify pricing decisions, or perform internal portfolio reviews.
        """)
    else:
        st.info("🔄 Adjust parameters and click **Simulate Impact** to explore outcomes.")


# ----------------------------------
# STEP 5: Decision-Ready Output
# ----------------------------------
elif page == "✅ Step 5: Decision-Ready Output":
    st.header("Step 5: Decision-Ready Output")
    st.image("step5_icon.png", width=100)

    st.markdown("""
    ### 🧾 Final Pricing Recommendation

    After completing all simulations and scenario tests, ARPU generates a **decision-ready quote packet** that is:

    - ✅ **Transparent** – all metrics are clearly defined  
    - ✅ **Clause-Aware** – aligned with submission context and coverage details  
    - ✅ **Risk-Optimized** – balancing margin, tail risk, and capital impact  
    - ✅ **Actionable** – ready to support broker or internal discussions

    ---
    """)

    recommendation = {
        "Recommended Retention": "$50M",
        "Limit": "$200M",
        "Rate-on-Line (ROL)": "10.8%",
        "Expected Loss": "$7.2M",
        "CVaR (99%)": "$22.5M",
        "ROI": "20.5%",
        "Underwriting Notes": "Balanced structure with acceptable tail risk and margin"
    }

    st.markdown("### 📋 Recommended Structure")
    st.table(pd.DataFrame.from_dict(recommendation, orient="index", columns=["Value"]))

    if st.button("📥 Generate Quote Packet"):
        st.success("✅ Your quote packet is ready. Preview below:")

        st.markdown("### 🧾 Quote Packet Preview")

        st.markdown("""
        **📌 Summary Recommendation:**  
        - **Retention:** `$50M`  
        - **Limit:** `$200M`  
        - **ROL:** `10.8%`  
        - **Expected Loss:** `$7.2M`  
        - **CVaR (99%):** `$22.5M`  
        - **ROI:** `20.5%`  

        **🧠 Underwriting Notes:**  
        Balanced structure with acceptable tail risk and margin.  
        Aligned with portfolio objectives and provides sufficient capital efficiency.

        ---

        ✅ This output can now be exported as a PDF or used in internal reviews.
        """)

        # Optional placeholder for download button
        st.download_button(
            label="⬇️ Download PDF (Coming Soon)",
            data="Quote packet content would go here.",
            file_name="ARPU_Quote_Packet.pdf",
            disabled=True
        )
