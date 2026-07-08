# Nexus Labs — Smart Health AI Platform

A multilingual, multi-agent AI platform for real-time monitoring and operational
management of Primary Health Centers (PHCs) and Community Health Centers (CHCs)
across a district.

Built for the **Smart Health – AI-Driven Health Center & Supply Chain Management** track.

## 💡 Overview

Nexus Labs is a multilingual, multi-agent AI platform built for real-time
monitoring and operational management of Primary Health Centers (PHCs) and
Community Health Centers (CHCs) across a district. Using a lightweight,
custom-chained agent architecture powered by the Gemini API, the platform
tracks medicine stock, bed availability, doctor attendance, and patient
footfall in real time. It automatically generates early stock-out warnings,
AI-driven demand forecasts, and smart resource redistribution recommendations
across a district's health centers — flagging underperforming or
under-resourced facilities to district administrators through a multilingual
executive report (English/Hindi). The result is faster intervention, reduced
medicine shortages, and better-informed district-level healthcare planning.

## ⚙️ How It Works

Instead of heavy multi-agent frameworks (CrewAI, LangChain), Nexus Labs uses a
custom, lightweight chained-function system built on the Gemini API. Four
autonomous agents run sequentially, each passing its output to the next:

1. **Inventory Analyst** — Monitors medicine stock %, triggers critical
   stock-out warnings below 20%, and produces demand forecasts.
2. **Operations & Capacity Auditor** — Evaluates bed availability, patient
   footfall, and doctor attendance; flags under-resourced facilities.
3. **Supply Chain & Redistribution Planner** — Combines Agent 1 & 2 outputs to
   recommend smart resource transfers between centers.
4. **Multilingual Admin Reporter** — Compiles the final plan into a crisp
   executive summary for district administrators in English or Hindi.

## 🎯 Target Audience

District health administrators, PHC/CHC facility managers, and state health
department officials responsible for resource allocation, supply chain
oversight, and healthcare quality monitoring across rural and semi-urban
districts.

## 🖥️ Tech Stack

- **Backend:** Python, Gemini API (`google-generativeai`)
- **Architecture:** Custom lightweight multi-agent chaining (no LangChain/CrewAI)
- **Frontend:** Streamlit — single-page real-time dashboard with red-alert
  panels, live operations view, logistics mapping, and downloadable
  multilingual reports
- **Data:** Structured JSON-based mock health center dataset (extensible to
  real-time district health data feeds)

## 📂 Project Structure
```
nexus-labs/
├── data/
│   └── district_health_centers_mock.json
├── agents/
│   ├── inventory_analyst.py
│   ├── operations_auditor.py
│   ├── redistribution_planner.py
│   └── admin_reporter.py
├── app.py
├── requirements.txt
└── README.md
```
## 🚧 Status
Work in progress — built for a 24-hour hackathon submission.

## 👥 Team
Himanshu Singhmar
Y Mounika
Nandhini
