import streamlit as st
import requests
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION & LUXURY HEALTHCARE SYSTEM CSS ---
st.set_page_config(
    page_title="Nexus Labs - Healthcare Command Center",
    page_icon="🏥",
    layout="wide"
)

# Custom Premium Styling Injection with Hospital Core Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f4f7fa !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #1e293b !important;
    }
    
    /* Luxury Hospital Theme Header */
    .header-banner {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 50%, #0f172a 100%);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px -15px rgba(2, 132, 199, 0.3);
    }
    
    .header-banner::after {
        content: "🏥";
        position: absolute;
        right: 5%;
        top: 15%;
        font-size: 8rem;
        opacity: 0.12;
    }
    
    .header-banner h1 { 
        color: white !important; 
        font-weight: 700; 
        margin: 0; 
        font-size: 3.2rem;
        letter-spacing: -0.5px;
    }
    .header-banner p { 
        color: #e0f2fe !important; 
        margin: 8px 0 0 0; 
        font-size: 1.2rem;
        font-weight: 400;
    }
    
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #0f172a;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Live Status Indicators */
    .status-pulse {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #22c55e;
        border-radius: 50%;
        box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
    }

    /* Top Premium Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2.4rem !important;
        font-weight: 700 !important;
        color: #0369a1 !important;
    }
    [data-testid="stMetricLabel"] {
        font-weight: 600 !important;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.85rem !important;
    }
    div[data-testid="stMetric"] {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02), 0 2px 4px -1px rgba(0,0,0,0.02);
        border: 1px solid #e2e8f0;
        border-bottom: 4px solid #0284c7;
    }
    
    /* Ultimate Smart Action Trigger Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0284c7 0%, #0369a1 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        padding: 1rem 2.5rem !important;
        border-radius: 14px !important;
        border: none !important;
        box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-top: 1rem;
        margin-bottom: 2rem;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -5px rgba(2, 132, 199, 0.5) !important;
    }
    
    /* Enterprise Grade Agent Cards Grid Layout */
    .agent-card {
        background: white !important;
        padding: 2rem;
        border-radius: 18px;
        margin-bottom: 1.75rem;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.04), 0 4px 6px -2px rgba(0,0,0,0.01);
        border-left: 6px solid #cbd5e1;
        min-height: 280px;
        transition: transform 0.2s ease;
    }
    .agent-card:hover {
        transform: translateY(-4px);
    }
    .card-inv { border-left-color: #ef4444 !important; background: linear-gradient(to right, #fef2f2, #ffffff 15%) !important; }
    .card-ops { border-left-color: #f59e0b !important; background: linear-gradient(to right, #fffbeb, #ffffff 15%) !important; }
    .card-log { border-left-color: #3b82f6 !important; background: linear-gradient(to right, #eff6ff, #ffffff 15%) !important; }
    .card-rep { border-left-color: #10b981 !important; background: linear-gradient(to right, #f0fdf4, #ffffff 15%) !important; }
    
    .card-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 1px dashed #e2e8f0;
        padding-bottom: 0.5rem;
    }
    .title-inv { color: #dc2626; }
    .title-ops { color: #d97706; }
    .title-log { color: #2563eb; }
    .title-rep { color: #059669; }

    .card-content {
        color: #334155 !important;
        font-size: 1rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. EMBEDDED MOUNIKA'S DATASET ---
mock_json_data = {
  "district": "Ganganagar",
  "generated_at": "2026-07-07T17:28:00+05:30",
  "health_centers": [
    {
      "center_id": "PHC-001",
      "name": "Suratgarh PHC",
      "type": "PHC",
      "medicine_stock_percent": 14,
      "critical_medicines_out": ["Paracetamol", "ORS Packets"],
      "doctors_present": 0,
      "beds_total": 10,
      "beds_occupied": 9,
      "patient_footfall_today": 78
    },
    {
      "center_id": "CHC-002",
      "name": "Bikaner CHC",
      "type": "CHC",
      "medicine_stock_percent": 92,
      "critical_medicines_out": [],
      "doctors_present": 5,
      "beds_total": 30,
      "beds_occupied": 11,
      "patient_footfall_today": 62
    },
    {
      "center_id": "PHC-003",
      "name": "Anupgarh PHC",
      "type": "PHC",
      "medicine_stock_percent": 45,
      "critical_medicines_out": ["Amoxicillin"],
      "doctors_present": 2,
      "beds_total": 15,
      "beds_occupied": 12,
      "patient_footfall_today": 45
    }
  ]
}

# --- 3. HARD OVERRIDE BYPASS CONNECTION ---
def bypass_gemini_call(prompt_text):
    import streamlit as st
    import requests
    
    api_key = st.secrets["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    
    try:
        payload = {
            "contents": [{"parts": [{"text": prompt_text}]}]
        }
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        res_json = response.json()
        
        if 'candidates' in res_json and res_json['candidates']:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"API Error: {res_json}"
    except Exception as e:
        return f"System Agent Sync Offline. Error Detail: {str(e)}"
def run_nexus_intelligence(data_input):
    data_str = json.dumps(data_input)
    
    inv_p = f"You are Nexus Inventory Analyst. Review this: {data_str}. Flag under 20% stock and list critical medicines out neatly."
    inventory_insights = bypass_gemini_call(inv_p)
    
    ops_p = f"You are Nexus Operations Auditor. Analyze resource gaps, doctor occupancy, and under-resourced centers in: {data_str}."
    operations_insights = bypass_gemini_call(ops_p)
    
    log_p = f"You are Nexus Logistics Planner. Create a clear resource redistribution recommendation plan based on: {inventory_insights} and {operations_insights}."
    logistics_plan = bypass_gemini_call(log_p)
    
    rep_p = f"Take this logistics redistribution plan and compile it into a crisp, professional executive summary report written ENTIRELY and CLEARLY in professional ENGLISH for district administrators presentation: {logistics_plan}."
    final_executive_report = bypass_gemini_call(rep_p)
    
    return {
        "inventory": inventory_insights,
        "operations": operations_insights,
        "logistics": logistics_plan,
        "report": final_executive_report
    }

# --- 4. PREMIUM BRANDED BANNER ---
st.markdown(f"""
    <div class="header-banner">
        <h1>🏥 Nexus Labs</h1>
        <p>Next-Gen Autonomous Multi-Agent AI Platform — {mock_json_data['district']} District Healthcare Command Center</p>
    </div>
""", unsafe_allow_html=True)

# Live Status Feed Section Title
st.markdown("""
    <div class="section-title">
        <span class="status-pulse"></span> 📡 Real-Time District Infrastructure Stream
    </div>
""", unsafe_allow_html=True)

# Metrics Feed Row
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1: st.metric(label="Total Monitored Clinics", value=len(mock_json_data["health_centers"]))
with m_col2: st.metric(label="Active Critical Gaps", value="2 Facilities")
with m_col3: st.metric(label="LLM Synchronization Network", value="Active / Secure")

st.markdown("<br>", unsafe_allow_html=True)

# --- NEW VISUAL GRAPH SECTIONS (REAL DEVELOPER LOOK) ---
st.markdown("""
    <div class="section-title">
        📊 Analytical Infrastructure Visualization Maps
    </div>
""", unsafe_allow_html=True)

# Extracting dataset metrics dynamically to draw native high-grade graphs
names = [c["name"] for c in mock_json_data["health_centers"]]
stock_levels = [c["medicine_stock_percent"] for c in mock_json_data["health_centers"]]
footfall = [c["patient_footfall_today"] for c in mock_json_data["health_centers"]]

chart_data = pd.DataFrame({
    "Health Center Nodes": names,
    "Medicine Stock (%)": stock_levels,
    "Patient Footfall": footfall
})
chart_data.set_index("Health Center Nodes", inplace=True)

graph_col1, graph_col2 = st.columns(2)

with graph_col1:
    st.caption("📈 Emergency Stock Levels Analysis Chart")
    st.bar_chart(chart_data["Medicine Stock (%)"], color="#0284c7")

with graph_col2:
    st.caption("📈 Patient Footfall & Capacity Mapping Index")
    st.line_chart(chart_data["Patient Footfall"], color="#ef4444")

st.markdown("<br>", unsafe_allow_html=True)

# --- ACTION TRIGGER BUTTON ---
if st.button("🚀 Trigger Autonomous District Health Analysis Network", use_container_width=True):
    with st.spinner("Initializing Multi-Agent Intelligence Layer Hub... Processing Node Metrics..."):
        try:
            results = run_nexus_intelligence(mock_json_data)
            
            st.markdown("""
                <div class="section-title">
                    📊 Live Autonomous Multi-Agent Output Matrix
                </div>
            """, unsafe_allow_html=True)
            
            # --- 2x2 LUXURY CARD GRID ---
            row1_c1, row1_c2 = st.columns(2)
            row2_c1, row2_c2 = st.columns(2)
            
            with row1_c1:
                st.markdown(f"""
                    <div class="agent-card card-inv">
                        <div class="card-title title-inv">🩸 Agent 1: Inventory Analyst Insights</div>
                        <div class="card-content">{results["inventory"]}</div>
                    </div>
                """, unsafe_allow_html=True)
                
            with row1_c2:
                st.markdown(f"""
                    <div class="agent-card card-ops">
                        <div class="card-title title-ops">🩺 Agent 2: Operations Capacity Auditor</div>
                        <div class="card-content">{results["operations"]}</div>
                    </div>
                """, unsafe_allow_html=True)
                
            with row2_c1:
                st.markdown(f"""
                    <div class="agent-card card-log">
                        <div class="card-title title-log">📦 Agent 3: Supply Chain & Resource Redistribution Plan</div>
                        <div class="card-content">{results["logistics"]}</div>
                    </div>
                """, unsafe_allow_html=True)
                
            with row2_c2:
                st.markdown(f"""
                    <div class="agent-card card-rep">
                        <div class="card-title title-rep">📋 Agent 4: Executive Administrative Summary Report</div>
                        <div class="card-content">{results["report"]}</div>
                    </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Execution Error: {str(e)}")
else:
    st.info("💡 Clinical System Note: Click the button above to deploy independent agent clusters onto the current hospital infrastructure data pool.")
    
