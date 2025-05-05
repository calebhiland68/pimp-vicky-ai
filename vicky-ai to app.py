import streamlit as st
import datetime

# Title
st.title("Pimp Vicky AI – Daily Stock Vibes")

# Date
today = datetime.date.today()
st.markdown(f"### Market Analysis for {today}")

# Placeholder content
st.success("Pimp Vicky has completed her daily analysis.")
st.write("Top tickers with good vibes today:")
st.write("- TSLA")
st.write("- AAPL")
st.write("- NVDA")
st.write("- AMZN")

# Refresh option
if st.button("Refresh Vibes"):
    st.info("Updated daily. Come back tomorrow for fresh moves.")