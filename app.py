import streamlit as st
from logic import get_price, get_sla
from rag import retrieve_context

st.title("ZENDS Smart Assistant 🚀")

# Structured Query
st.header("📊 Pricing Lookup")

product = st.selectbox("Product", ["Prepaid Basic"])
country = st.selectbox("Country", ["USA", "India"])
user_type = st.selectbox("User Type", ["individual", "enterprise"])

if st.button("Get Price"):
    price = get_price(product, country, user_type)
    st.success(f"Price: ${price}")

# SLA
st.header("📈 SLA Info")

sla_type = st.selectbox("User Type for SLA", ["individual", "enterprise"])

if st.button("Get SLA"):
    st.info(get_sla(sla_type))

# RAG Chat
st.header("🤖 Ask Anything")

query = st.text_input("Ask about ZENDS")

if st.button("Ask"):
    context = retrieve_context(query)
    st.write(context)