# 🛡️ Aiden: Intelligent Treaty Structuring Assistant

**Aiden** is an **AI co‑pilot for reinsurance treaty underwriters** that accelerates treaty structuring from **weeks to minutes**.
It combines **LLM‑powered contract comprehension** with **RL‑driven optimization** to help underwriters **analyze, simulate, and design optimal treaty structures**—all through an **interactive 5‑step demo**.

🔗 **Live Demo:** [Click here to try Aiden](https://stellacydong-intelligent-treaty-structuring-assistan-app-7ccyqq.streamlit.app)

---

## 🌟 Key Features

1. **Reads & Summarizes Treaty Wordings**

   * Instantly parses complex reinsurance contracts, cedent submissions, and historical losses.
   * Produces structured, underwriter‑ready summaries.

2. **RL‑Based Treaty Structure Optimization**

   * Simulates thousands of treaty variations (retentions, limits, layers).
   * Identifies structures that maximize ROI under tail‑risk constraints.

3. **Interactive What‑If Analysis**

   * Adjust key parameters (e.g., attachment point).
   * See immediate impact on **expected loss** and **projected ROI**.

4. **Conversational AI for Treaty Design**

   * Chat naturally with **Aiden**:

     > “What if we split into two layers instead?”
   * Streaming, human‑like responses with context awareness.

5. **Final Recommendation + Risk Heatmap**

   * Aiden recommends the **top structure** with clear rationale.
   * Visual **risk vs. return landscapes** and heatmaps for intuitive decision‑making.

---

## 📂 Project Structure

```
aiden-treaty-demo/
├── app.py               # Main Streamlit application (5‑step demo)
├── requirements.txt     # Python dependencies for Streamlit Cloud
├── logo.png             # Company / Product logo
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/aiden-treaty-demo.git
cd aiden-treaty-demo
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open the provided **local URL** (usually `http://localhost:8501`).

---

## 🌐 Deploying to Streamlit Cloud

1. Push your repo to **GitHub**.
2. Create a new app at [share.streamlit.io](https://share.streamlit.io).
3. Select the repo and branch, and set the **main file** to `app.py`.
4. Add **`requirements.txt`** for dependencies.

Your app will be **live in minutes**.

🔹 **Current Live App:**
[https://stellacydong-intelligent-treaty-structuring-assistan-app-7ccyqq.streamlit.app](https://stellacydong-intelligent-treaty-structuring-assistan-app-7ccyqq.streamlit.app)

---

## 📊 Demo Flow

1. **Step 1: Treaty Summary**

   > Use sample treaty → Aiden generates a structured summary.

2. **Step 2: RL Optimization**

   > Explore candidate structures with a **risk‑reward scatterplot** and ROI benchmark.

3. **Step 3: What‑If Analysis**

   > Adjust attachment points → Instantly see ROI and loss changes.

4. **Step 4: Chat with Aiden**

   > Ask scenario questions and receive **context‑aware streaming responses**.

5. **Step 5: Final Recommendation**

   > Get the **recommended structure**, risk heatmap, and narrated rationale.

---

## 🧠 Why Aiden Matters

Reinsurance treaty structuring is **slow, expensive, and opaque**.
Each deal requires **weeks of actuarial, underwriting, and legal work**, often costing **tens of thousands of dollars upfront**.

Aiden:

* Makes **smaller deals economical**
* **Scales expert knowledge** for underwriters and brokers
* Unlocks **faster, smarter, and more transparent** reinsurance markets

---

## 📄 License

MIT License – Free to use and modify for demos and research.

