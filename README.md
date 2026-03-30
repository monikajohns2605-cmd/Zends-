# Zends-
A full-stack intelligent telecom system that combines structured data + business logic + AI (RAG) to deliver accurate pricing, SLA, and service insights.

📌 Overview

ZENDS Smart Assistant is designed to simulate a real-world telecom platform based on the ZENDS Communications specification. It supports:

📊 Structured product pricing queries
📈 SLA and policy retrieval
🤖 AI-powered question answering (RAG)
🌐 API-based access
🎨 Interactive UI using Streamlit
🏗️ Architecture
User Input
   ↓
Query Classifier
   ↓
 ┌───────────────┬───────────────┐
 │ Structured    │ Unstructured  │
 │ (DB + Logic)  │ (RAG + FAISS) │
 └───────────────┴───────────────┘
         ↓
     Streamlit UI / FastAPI
🧩 Features
✅ Structured System
Product pricing by country and user type
SLA retrieval (Individual, Business, Enterprise)
Discount logic
🤖 AI Capabilities
Semantic search using Sentence Transformers
FAISS-based vector retrieval
Natural language query support
🌐 API Support
REST endpoints using FastAPI
Easy integration with external systems
🎨 UI
Streamlit-based interactive dashboard
Dropdown filters + chatbot interface
📁 Project Structure
zends_project/
│
├── app.py              # Streamlit UI
├── api.py              # FastAPI backend
├── db.py               # Database setup
├── logic.py            # Business logic
├── rag.py              # AI retrieval system
├── utils.py            # Helper functions
├── requirements.txt
└── zends.db            # SQLite database
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/zends-project.git
cd zends-project
2. Create virtual environment
python -m venv venv
3. Activate environment
venv\Scripts\activate   # Windows
4. Install dependencies
pip install -r requirements.txt
🗄️ Initialize Database
python
from db import create_tables, seed_data
create_tables()
seed_data()
exit()
▶️ Run the Application
🚀 Start Streamlit UI
streamlit run app.py
🌐 Start API (optional)
uvicorn api:app --reload

Open:

http://127.0.0.1:8000/docs
🧪 Example Queries
📊 Structured
Price of Prepaid Basic in USA (individual)
SLA for enterprise users
🤖 AI Queries
What services does ZENDS provide?
What is the refund policy?
Explain cloud services
📊 Tech Stack
Python
Streamlit
FastAPI
SQLite
Sentence Transformers
FAISS
Transformers (Hugging Face)
🎯 Future Improvements
Full dataset integration (all products)
Advanced query understanding (NLP routing)
Chat memory
Deployment (AWS / Render)
Role-based access
📜 License

This project is for educational and demonstration purposes.

🙌 Acknowledgements

Inspired by telecom system design and real-world service architectures.
