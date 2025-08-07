# ⚡ ARPU Pricing Co-Pilot

**Adaptive Risk Pricing & Underwriting (ARPU)** is an AI-powered pricing assistant for reinsurance underwriters.  
This Streamlit demo walks users through a 5-step underwriting workflow — from raw submission intake to optimized, decision-ready treaty quotes.

---

## 🚀 Demo Overview

This interactive demo showcases how ARPU leverages LLMs and reinforcement learning to automate and enhance the treaty pricing workflow.

### 🧭 Workflow Steps

1. **📁 File Intake & Parsing**  
   Upload or preview reinsurance submissions in PDF, CSV, or XLSX format. ARPU extracts key fields like TIV, loss history, CAT model outputs, and exposures.

2. **🧠 AI-Powered Summarization**  
   A fine-tuned Large Language Model (LLM) parses raw documents and generates a structured submission summary with underwriting signals and risk metrics.

3. **📈 Simulation & Optimization**  
   A Reinforcement Learning (RL) agent explores multiple retention-limit-ROL combinations to generate a set of candidate treaty structures based on expected loss, CVaR, and ROI.

4. **🧮 Interactive Insights**  
   Users can test custom scenarios by adjusting retention, limit, and CAT severity to simulate performance under various treaty configurations.

5. **✅ Decision-Ready Output**  
   ARPU recommends an optimized structure aligned with capital, margin, and tail risk constraints. The final quote packet is previewed and (optionally) downloadable.

---

## 🖼️ Screenshots

| Step | Description |
|------|-------------|
| 🏠 Home | Overview and flow diagram |
| 📁 Step 1 | Upload and parse submission files |
| 🧠 Step 2 | Summarize with LLM |
| 📈 Step 3 | Optimize pricing via RL |
| 🧮 Step 4 | Run what-if CAT scenarios |
| ✅ Step 5 | View and download final quote |

---

## 🧱 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Backend**: Python (LLM + RL simulation)
- **Libraries**: `pandas`, `datetime`, `random`, `time`
- **Design**: Custom iconography and flow images (`step1_icon.png` to `step5_icon.png`, `How_ARPU_Works.png`, `logo.png`)

---

## 📂 File Structure

```

📦 arpu-pricing-demo
├── app.py                  # Main Streamlit script
├── logo.png
├── How\_ARPU\_Works.png
├── step1\_icon.png
├── step2\_icon.png
├── step3\_icon.png
├── step4\_icon.png
├── step5\_icon.png
└── README.md

````

---

## 🔧 Setup Instructions

### 📍 Requirements
```bash
pip install streamlit pandas
````

### ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Inspiration

Reinsurance treaty pricing is traditionally time-consuming, opaque, and highly manual.
ARPU demonstrates how AI can enhance transparency, speed, and strategic optimization across the entire pricing workflow.

---

## 📬 Contact

Built by **\[Reinsurance Analytics]**
If you’d like to integrate ARPU into your underwriting workflow, reach out at \[[contact@reinsuranceanalytics.io](mailto:contact@reinsuranceanalytics.io)].

---

