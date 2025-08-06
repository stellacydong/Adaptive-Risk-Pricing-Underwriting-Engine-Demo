import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import time

# =====================
# 1. PAGE CONFIG
# =====================
st.set_page_config(
    page_title="Intelligent Treaty Structuring Assistant — YC Demo",
    layout="wide"
)


# =====================
# 3. SIDEBAR NAVIGATION
# =====================
st.sidebar.title("Demo Navigation")
page = st.sidebar.radio(
    "Select a demo feature:",
    ["🏠 Home", "📄 Step 1: Treaty Summary", "📈 Step 2: RL Optimization",
     "🎛 Step 3: What‑If Analysis", "💬 Step 4: Chat with Aiden", "📊 Step 5: Final Recommendation"]
)

# =====================
# 4. GLOBAL STATE
# =====================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "treaty_summary" not in st.session_state:
    st.session_state.treaty_summary = None
if "recommended_structures" not in st.session_state:
    st.session_state.recommended_structures = None
if "selected_attachment" not in st.session_state:
    st.session_state.selected_attachment = 50

# =====================
# 5. HELPER FUNCTIONS
# =====================
LONG_TREATY = """
Cedent: Example Insurance Co.
Program: 2025 U.S. Catastrophe Excess of Loss Treaty (Property Cat XoL)
...
(Full treaty text)
"""

def generate_summary():
    return """
**Summary of Uploaded Treaty (2025 Cat XoL Program)**

This treaty provides **property catastrophe excess-of-loss coverage** for **Example Insurance Co.**  
in the **continental U.S., Hawaii, and Puerto Rico** for **January 1 – December 31, 2025**.

- **Program Structure:** 5 × 50 M layers excess 50 M → **300 M limit**, 50 M attachment  
- **Reinstatements:** 1 × 100% paid, subsequent at 125%  
- **Covered Perils:** Hurricanes, typhoons, floods (168‑hour clause)  
- **Exclusions:** War, terrorism, nuclear  
- **Special Conditions:** 14‑day loss reporting, 30‑day interim updates, ARIAS‑U.S. arbitration  

**Historical Losses:** 70M, 38M, 45M, 92M (Hurricanes & Hail)  

**Key Takeaways:**  
High exposure to hurricanes and hail with mid‑layer protection.  
Opportunities exist to **adjust attachment points and layering** for better ROI and risk balance.
"""

def simulate_rl_structures(attach_point=50, n=5):
    structures = []
    for _ in range(n):
        layers = random.randint(1, 3)
        limit = random.choice([50, 75, 100])
        expected_loss = round(random.uniform(10, 80), 2)
        roi = round(random.uniform(5, 25), 2)
        structures.append([f"{layers} x {limit}M XS {attach_point}M", expected_loss, roi])
    df = pd.DataFrame(structures, columns=["Structure", "Expected Loss (M)", "Projected ROI (%)"])
    st.session_state.recommended_structures = df
    return df

def what_if_analysis(attach_point):
    loss_change = round(random.uniform(-20, 20), 2)
    roi_change = round(random.uniform(-5, 5), 2)
    return loss_change, roi_change

def simulated_chat_response(user_input):
    summary_context = st.session_state.treaty_summary or "a mid-layer catastrophe treaty with 50M attachment."
    return f"Considering {summary_context[:80]}..., {user_input.lower()} may improve ROI and balance tail risk under hurricane and hail scenarios."

def plot_risk_heatmap(df):
    heatmap_data = np.random.rand(5, 5)
    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, cmap="YlOrRd", cbar=True, ax=ax)
    ax.set_title("Risk Heatmap: Loss Severity vs. ROI", fontsize=14)
    ax.set_xlabel("ROI Quintile")
    ax.set_ylabel("Loss Severity Quintile")
    return fig

# =====================
# 6. DEMO PAGES
# =====================

# 1. Home
if page == "🏠 Home":
    # =====================
    # Hero Section
    # =====================
    st.image("logo.png", width=220)
    st.markdown(
        """
        <h1 style='text-align: center;'>🤖 Aiden — AI Treaty Co‑Pilot</h1>
        <h3 style='text-align: center; font-weight: 400;'>
        Design, simulate, and optimize reinsurance treaties <b>in minutes</b>, not weeks.
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # =====================
    # Product Overview
    # =====================
    st.markdown(
        """
        ### 🌟 Product Overview
        **Aiden** is your AI‑powered assistant for reinsurance treaty structuring.  
        It reads treaty wordings, optimizes risk structures with **reinforcement learning**,  
        and provides interactive, explainable recommendations for underwriters.
        """
    )

    # =====================
    # Key Features
    # =====================
    st.markdown("### 🔑 Key Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 📄 Smart Treaty Parsing")
        st.write("Uploads PDFs or data sheets and instantly summarizes clauses, layers, and exclusions.")
    with col2:
        st.markdown("#### 📈 RL‑Based Optimization")
        st.write("Finds high‑ROI treaty structures via risk simulations and multi‑scenario RL agents.")
    with col3:
        st.markdown("#### 💬 Interactive What‑If Chat")
        st.write("Ask natural language questions and explore alternative treaty designs instantly.")

    # =====================
    # How It Works
    # =====================
    st.markdown("---")
    st.markdown("### ⚡ How Aiden Works")
    steps = [
        "1️⃣ **Upload Treaty Data** – PDFs or structured cedent data",
        "2️⃣ **AI Reads & Summarizes** – Key layers, clauses, and historical loss insights",
        "3️⃣ **RL Simulates Structures** – Multi‑scenario optimization for ROI & risk balance",
        "4️⃣ **Interactive What‑If Chat** – Explore ideas like 'Split into two layers?' instantly",
        "5️⃣ **Final Recommendation** – Optimized structure + risk heatmap for decision‑makers"
    ]
    for step in steps:
        st.markdown(step)

    # =====================
    # Why It Matters / Market Context
    # =====================
    st.markdown("---")
    st.markdown(
        """
        ### 🚀 Why Aiden Matters
        - Global reinsurance is a **$500B market** still running on emails and manual spreadsheets  
        - Treaty structuring can take **4–6 weeks** with opaque pricing and slow iterations  
        - AI makes **real‑time treaty optimization** finally possible  
        
        **Aiden turns weeks of work into minutes, helping insurers move faster and smarter.**
        """
    )

    # =====================
    # Call to Action
    # =====================
    st.markdown("---")
    st.markdown(
        """
        <h3 style='text-align: center;'>
        🏁 Ready to see Aiden in action?  
        Use the sidebar to explore our 5‑step demo →
        </h3>
        """,
        unsafe_allow_html=True
    )


# 2. Step 1: Treaty Summary
elif page == "📄 Step 1: Treaty Summary":
    st.markdown("## 📄 Step 1: AI Reads & Summarizes Treaty Wordings")

    st.markdown(
        """
        **Aiden** starts by reading full treaty wordings — complex, multi‑page legal documents —  
        and instantly generates a **structured, underwriter‑friendly summary**.  

        For this demo, we’re using a **sample treaty** to show how Aiden works:
        """
    )

    st.code(LONG_TREATY, language="text")

    # Optional upload teaser for future version
    st.caption("🔹 *Pro version will let you upload your own treaty PDFs for instant AI analysis.*")

    if st.button("✨ Generate AI Summary"):
        with st.spinner("Aiden is reviewing clauses, calculating exposures, and summarizing key terms..."):
            time.sleep(1.5)
            summary = generate_summary()

        st.success("✅ AI‑Generated Treaty Summary")
        st.markdown(summary)

        st.session_state.treaty_summary = summary

        # Polished explanation with icons
        st.markdown(
            """
            ### 💡 Why This Step Matters
            - ⚡ **Instant Overview** – Turns dense treaty wordings into a clear executive summary  
            - 🛡 **Key Risk Highlights** – Identifies exposures, historical losses, and critical clauses  
            - 🔗 **Seamless Workflow** – Feeds directly into **Step 2: RL‑Based Optimization**  
            """
        )


# 3. Step 2: RL Optimization
elif page == "📈 Step 2: RL Optimization":
    st.markdown("## 📈 Step 2: RL‑Based Treaty Structure Optimization")
    
    st.markdown(
        """
        After the treaty is summarized in **Step 1**, **Aiden** uses a **Reinforcement Learning (RL) engine**  
        to simulate market scenarios and **propose optimized treaty structures** that maximize ROI  
        while managing tail risk.
        """
    )

    if not st.session_state.treaty_summary:
        st.warning("⚠️ Please complete Step 1 first to generate a treaty summary.")
    else:
        attach = st.session_state.selected_attachment
        df = simulate_rl_structures(attach)

        st.markdown("### 🏗 Proposed Treaty Structures (Simulated)")
        st.dataframe(df, use_container_width=True)

        # Highlight top candidate
        best_row = df.sort_values(by="Projected ROI (%)", ascending=False).iloc[0]
        st.success(
            f"**Top Candidate:** {best_row['Structure']}  \n"
            f"Expected Loss: **{best_row['Expected Loss (M)']}M**  \n"
            f"Projected ROI: **{best_row['Projected ROI (%)']}%**"
        )

        # =====================
        # Professional Risk vs. Return Plot
        # =====================
        st.markdown("### 📊 Risk vs. Return Landscape")

        fig, ax = plt.subplots(figsize=(6, 4))  # compact professional figure
        scatter = ax.scatter(
            df["Expected Loss (M)"],
            df["Projected ROI (%)"],
            c=df["Projected ROI (%)"],
            cmap="viridis",
            s=100, edgecolors="black", alpha=0.85
        )

        # Annotate top candidate
        ax.text(
            best_row["Expected Loss (M)"] + 0.5,
            best_row["Projected ROI (%)"] + 0.3,
            "⭐ Top Candidate", fontsize=9, weight="bold", color="darkgreen"
        )

        # Add horizontal ROI benchmark line
        roi_benchmark = 15
        ax.axhline(y=roi_benchmark, color="red", linestyle="--", alpha=0.6, linewidth=1.2)
        ax.text(
            df["Expected Loss (M)"].max() * 0.95, roi_benchmark + 0.3,
            f"ROI Benchmark ({roi_benchmark}%)",
            fontsize=8, color="red", ha="right"
        )

        # Axis labels & title
        ax.set_xlabel("Expected Loss (Million $)", fontsize=11)
        ax.set_ylabel("Projected ROI (%)", fontsize=11)
        ax.set_title("Simulated Treaty Structures: Balancing Loss & Return", fontsize=13)
        ax.grid(alpha=0.3)

        # Add colorbar for ROI
        fig.colorbar(scatter, label="Projected ROI (%)")
        st.pyplot(fig)

        # Caption / Explanation
        st.caption(
            """
            **Figure:** Each point represents a simulated treaty structure evaluated by Aiden.  
            - **X-axis:** Expected Loss in millions of dollars  
            - **Y-axis:** Projected ROI (%)  
            - **Color Gradient:** Higher ROI shown in yellow-green  
            - **Dashed Red Line:** 15% ROI benchmark for strong performance  
            - **Top Candidate (⭐)** balances high ROI with moderate expected loss  
            """
        )

        # Context for next step
        st.markdown(
            """
            ### 💡 Why This Matters
            - **Visualizes trade‑off** between expected loss and return  
            - **Benchmark line** quickly shows which structures outperform a 15% ROI goal  
            - **Top Candidate** highlights the best balance for current market conditions  

            ➡ Proceed to **Step 3** for interactive **What‑If Analysis**.
            """
        )


# 4. Step 3: What‑If Analysis
elif page == "🎛 Step 3: What‑If Analysis":
    st.markdown("## 🎛 Step 3: Interactive What‑If Analysis")

    st.markdown(
        """
        In this step, **Aiden** allows underwriters to **explore alternative treaty structures**  
        by adjusting the **attachment point** (the level of loss at which reinsurance kicks in).  

        - Lower attachment points → Higher reinsurer exposure but faster coverage  
        - Higher attachment points → Lower expected loss but reduced ROI potential  
        
        Use the slider below to simulate **how different attachment points affect ROI and expected loss**.
        """
    )

    # =====================
    # 1. Interactive Slider
    # =====================
    attach_point = st.slider(
        "Select Attachment Point (Million $)",
        min_value=10, max_value=100,
        value=st.session_state.selected_attachment, step=5
    )

    # =====================
    # 2. Run What‑If Simulation
    # =====================
    if st.button("🔮 Analyze Impact"):
        st.session_state.selected_attachment = attach_point

        # Compute simulated changes
        loss_change, roi_change = what_if_analysis(attach_point)

        st.success(
            f"""
            **Scenario Results for Attachment = {attach_point}M**  
            - 📉 Expected Loss changes by **{loss_change}%**  
            - 💹 Projected ROI changes by **{roi_change}%**
            """
        )

        # Generate updated RL‑optimized structures
        df = simulate_rl_structures(attach_point)

        # =====================
        # 3. Show Updated Table
        # =====================
        st.markdown("### 🏗 Updated RL‑Optimized Treaty Structures")
        st.dataframe(df, use_container_width=True)

        # Highlight the top candidate structure
        best_row = df.sort_values(by="Projected ROI (%)", ascending=False).iloc[0]
        st.info(
            f"""
            **Top Candidate at {attach_point}M Attachment:**  
            - Structure: **{best_row['Structure']}**  
            - Expected Loss: **{best_row['Expected Loss (M)']}M**  
            - Projected ROI: **{best_row['Projected ROI (%)']}%**
            """
        )

        # =====================
        # 4. Optional Visual: ROI vs. Loss
        # =====================
        st.markdown("### 📊 Risk vs. Return for Selected Attachment")
        fig, ax = plt.subplots(figsize=(6, 4))
        scatter = ax.scatter(
            df["Expected Loss (M)"],
            df["Projected ROI (%)"],
            c=df["Projected ROI (%)"],
            cmap="plasma",
            s=90, edgecolors="black", alpha=0.85
        )

        # Benchmark ROI line (15%)
        roi_benchmark = 15
        ax.axhline(y=roi_benchmark, color="red", linestyle="--", alpha=0.7)
        ax.text(
            df["Expected Loss (M)"].max() * 0.95, roi_benchmark + 0.3,
            f"ROI Benchmark ({roi_benchmark}%)",
            fontsize=8, color="red", ha="right"
        )

        # Annotate top candidate
        ax.text(
            best_row["Expected Loss (M)"] + 0.5,
            best_row["Projected ROI (%)"] + 0.3,
            "⭐ Top Candidate",
            fontsize=9, weight="bold", color="darkgreen"
        )

        ax.set_xlabel("Expected Loss (Million $)")
        ax.set_ylabel("Projected ROI (%)")
        ax.set_title(f"Impact of {attach_point}M Attachment", fontsize=13)
        ax.grid(alpha=0.3)
        fig.colorbar(scatter, label="Projected ROI (%)")

        st.pyplot(fig)

        # Figure Caption
        st.caption(
            f"""
            **Figure:** Simulated treaty structures with an attachment of {attach_point}M.  
            - **X-axis:** Expected Loss (M$)  
            - **Y-axis:** Projected ROI (%)  
            - **Dashed Red Line:** 15% ROI benchmark  
            - **Top Candidate (⭐):** Highest ROI for current attachment scenario
            """
        )

        # Context for moving forward
        st.markdown(
            """
            ### 💡 Key Insight
            Adjusting the attachment point **shifts the risk-return profile**.  
            Use this to find a **sweet spot** balancing profitability with acceptable risk.  
            
            ➡ Continue to **Step 4: Chat with Aiden** to explore these findings interactively.
            """
        )


# 5. Step 4: Chat Simulation (Streaming)
elif page == "💬 Step 4: Chat with Aiden":
    # --- Layout: Left Chat, Right Context Panel ---
    st.markdown("## 💬 Step 4: Interactive Chat with **Aiden**, Your Treaty AI Co‑Pilot")
    st.markdown(
        """
        Aiden understands your treaty and has simulated multiple structures.  
        Now, interact with Aiden in **natural language** to explore *what‑if* scenarios,  
        test alternative structures, and get explanations behind each recommendation.
        """
    )

    left_col, right_col = st.columns([2, 1])

    # ==========================
    # Left Column: Chat Interface
    # ==========================
    with left_col:
        st.markdown("### 🗨 Chat Interface")
        st.markdown(
            """
            **Example prompts:**  
            - *“What if we split the 50M limit into two 25M layers?”*  
            - *“How does raising the attachment to 75M affect ROI?”*  
            - *“Suggest a structure with ROI > 15% and low tail risk.”*  
            """
        )

        # Display Chat History
        for msg in st.session_state.chat_history:
            role_label = "👤 **You:**" if msg["role"] == "you" else "🤖 **Aiden:**"
            st.markdown(f"{role_label} {msg['content']}")

        # Input + Send
        user_input = st.text_input("💡 Type your question and press **Send**:")
        if st.button("Send") and user_input.strip():
            st.session_state.chat_history.append({"role": "you", "content": user_input})

            # Thinking Animation
            thinking_placeholder = st.empty()
            for _ in range(6):
                for dots in ["", ".", "..", "...", "....", "...", "..", "."]:
                    thinking_placeholder.markdown(
                        f"<span style='font-weight:bold; font-size:16px;'>🤖 Aiden is thinking{dots}</span>",
                        unsafe_allow_html=True
                    )
                    time.sleep(0.2)
            thinking_placeholder.empty()

            # Simulated Streaming Response
            full_response = simulated_chat_response(user_input)
            placeholder = st.empty()
            streamed_text = ""
            for word in full_response.split():
                streamed_text += word + " "
                placeholder.markdown(f"**🤖 Aiden:** {streamed_text}▌")
                time.sleep(random.uniform(0.04, 0.12))

            placeholder.markdown(f"**🤖 Aiden:** {full_response}")
            st.session_state.chat_history.append({"role": "Aiden", "content": full_response})

    # ==========================
    # Right Column: Context Panel
    # ==========================
    with right_col:
        st.markdown("### 📊 Current Treaty Context")
        
        # Current attachment point
        current_attach = st.session_state.get("selected_attachment", 50)
        
        # Get top candidate from last simulation
        if "last_simulated_df" in st.session_state:
            df = st.session_state.last_simulated_df
            top_candidate = df.sort_values(by="Projected ROI (%)", ascending=False).iloc[0]
            top_structure = top_candidate["Structure"]
            top_roi = top_candidate["Projected ROI (%)"]
        else:
            top_structure = "50 x 50M (default)"
            top_roi = 14.5

        roi_benchmark = 15.0
        benchmark_status = "✅ Above Benchmark" if top_roi >= roi_benchmark else "⚠ Below Benchmark"

        # Display Context Info
        st.metric(label="Current Attachment", value=f"{current_attach}M")
        st.metric(label="Top Candidate Structure", value=top_structure)
        st.metric(label="Top Projected ROI", value=f"{top_roi:.1f}%", delta=f"Target {roi_benchmark}%")
        st.markdown(f"**Status:** {benchmark_status}")

        st.markdown(
            """
            ---
            **Why this panel?**  
            - Keeps you aware of the **current scenario**  
            - Highlights **best structure** as Aiden evaluates options  
            - Benchmarks ROI vs a target for clear decision-making
            """
        )

    st.markdown("---")
    st.markdown(
        """
        **Next:** Continue to **Step 5: Final Recommendation & Risk Heatmap**  
        to see Aiden’s ultimate recommendation and visualize risk-return tradeoffs.
        """
    )

# 6. Step 5: Final Recommendation + Risk Heatmap
elif page == "📊 Step 5: Final Recommendation":
    st.markdown("## 📊 Step 5: Final Treaty Recommendation & Risk Heatmap")
    st.markdown(
        """
        In this final step, **Aiden** presents its top treaty structure recommendation  
        with a narrative that reflects the **chat and analysis** from previous steps.  
        """
    )

    df = st.session_state.get("recommended_structures", None)
    chat_history = st.session_state.get("chat_history", [])

    if df is not None and not df.empty:
        # --- 1. Identify Best Structure ---
        best_structure = df.sort_values(by="Projected ROI (%)", ascending=False).iloc[0]

        # --- 2. Narrative Summary Based on Chat Context ---
        recent_questions = [msg['content'] for msg in chat_history if msg['role'] == "you"][-2:]
        context_summary = (
            f"Aiden considered your {' and '.join(recent_questions)} queries "
            if recent_questions else
            "Aiden reviewed your previous what‑if explorations "
        )
        narrative_reason = (
            f"{context_summary}and optimized for a balance of **expected loss**, **ROI**, and **tail risk**. "
            f"This recommendation aligns with the scenarios we analyzed in Step 3 and your guidance in Step 4."
        )

        # --- 3. Recommendation Card ---
        st.markdown("### 🏆 Recommended Structure")
        st.success(
            f"""
            **Optimal Structure:** **{best_structure['Structure']}**  
            **Expected Loss:** {best_structure['Expected Loss (M)']:.1f} M  
            **Projected ROI:** {best_structure['Projected ROI (%)']:.1f}%  
            **CVaR (Tail Risk):** {best_structure.get('CVaR (%)', 12.0):.1f}%  
            """
        )

        # --- 4. Narrative Output ---
        st.markdown(f"**🤖 Aiden’s Rationale:** {narrative_reason}")

        st.markdown(
            """
            **Why this works:**  
            - Balances **expected loss and tail risk** for catastrophe scenarios  
            - Achieves a **strong ROI** vs the 15% benchmark  
            - Reflects **chat‑driven what‑if exploration** and RL optimization  
            """
        )

        # --- 5. Risk Heatmap ---
        st.markdown("### 🌡 Risk vs. Return Landscape")
        fig, ax = plt.subplots(figsize=(6, 4))
        scatter = ax.scatter(
            df["Expected Loss (M)"],
            df["Projected ROI (%)"],
            c=df.get("CVaR (%)", [12]*len(df)),
            cmap="coolwarm",
            s=80,
            edgecolors="black"
        )

        # Highlight the best structure
        ax.scatter(
            best_structure["Expected Loss (M)"],
            best_structure["Projected ROI (%)"],
            color="gold",
            edgecolors="black",
            s=150,
            label="🏆 Recommended"
        )

        # Annotate structures
        for i, row in df.iterrows():
            ax.text(
                row["Expected Loss (M)"],
                row["Projected ROI (%)"] + 0.4,
                row["Structure"],
                fontsize=7, ha='center'
            )

        # Add ROI benchmark line
        roi_benchmark = 15
        ax.axhline(y=roi_benchmark, color="green", linestyle="--", linewidth=1)
        ax.text(df["Expected Loss (M)"].min(), roi_benchmark + 0.3, "ROI Benchmark (15%)", color="green", fontsize=8)

        ax.set_xlabel("Expected Loss (Million $)")
        ax.set_ylabel("Projected ROI (%)")
        ax.set_title("Risk / Return Heatmap")
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label("CVaR (%) - Tail Risk")
        st.pyplot(fig)

        # --- 6. Contextual Explanation ---
        st.markdown(
            """
            **How to interpret this view:**  
            - **Gold point:** Aiden’s recommended structure  
            - **Dashed line:** ROI benchmark (15%) for reference  
            - **Cooler colors:** Lower tail risk (CVaR)  
            - **Narrative:** Connects recommendation to your Step 4 chat explorations  
            """
        )

        st.markdown("✅ **Demo Complete:** Aiden reads, simulates, chats, and delivers an explainable treaty recommendation in minutes.")
    else:
        st.warning("⚠ Please run Steps 2–3 to generate optimized structures before viewing Step 5.")
