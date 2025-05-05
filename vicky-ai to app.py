import streamlit as st
import datetime
import yfinance as yf

st.set_page_config(page_title="Pimp Vicky – Stock AI", page_icon="💰")
st.title("Pimp Vicky – Your Stock Market Baddie")

# Init state
if "step" not in st.session_state:
    st.session_state.step = "greeting"
if "investment" not in st.session_state:
    st.session_state.investment = None
if "style" not in st.session_state:
    st.session_state.style = None
if "ticker" not in st.session_state:
    st.session_state.ticker = None

# --- Step Flow ---
if st.session_state.step == "greeting":
    st.markdown("**Vicky:** Hey sugar, I'm Vicky — your AI stock plug. Let's run this bag up.")
    if st.button("Let's go"):
        st.session_state.step = "ask_investment"

elif st.session_state.step == "ask_investment":
    investment = st.number_input("**Vicky:** How much money you lookin’ to invest today?**", min_value=10.0)
    if st.button("Lock it in"):
        st.session_state.investment = investment
        st.session_state.step = "ask_style"

elif st.session_state.step == "ask_style":
    style = st.radio("**Vicky:** You ridin’ this wave short-term or sittin’ pretty long-term?**", ["Day Trading", "Long-Term"])
    if st.button("Pick your hustle"):
        st.session_state.style = style
        st.session_state.step = "ask_prediction"

elif st.session_state.step == "ask_prediction":
    want_prediction = st.radio("**Vicky:** Want me to run a prediction on your investment for today?**", ["Yes", "No"])
    if want_prediction == "Yes":
        st.session_state.step = "get_ticker"
    elif want_prediction == "No":
        st.markdown("**Vicky:** Aight. You know where to find me when you're ready.**")

elif st.session_state.step == "get_ticker":
    ticker = st.text_input("**Vicky:** Drop the stock ticker, baby. Let me work my magic.**").upper()
    if st.button("Show me the money"):
        st.session_state.ticker = ticker
        st.session_state.step = "predict"

elif st.session_state.step == "predict":
    ticker = st.session_state.ticker
    investment = st.session_state.investment
    style = st.session_state.style

    try:
        data = yf.download(ticker, period="5d", interval="1d")
        last_close = data['Close'][-1]
        predicted_price = last_close * (1.01 if style == "Day Trading" else 1.05)
        estimated_return = (predicted_price - last_close) / last_close * investment

        st.markdown(f"**Vicky:** Stock `{ticker}` closed at **${last_close:.2f}**.")
        st.markdown(f"**Vicky:** I’m seeing a target of **${predicted_price:.2f}** by next session.")
        st.markdown(f"**Vicky:** If you invest ${investment}, I’m projecting **${estimated_return:.2f}** in returns.")

        st.balloons()
        st.markdown("**Vicky:** Stay sharp, keep that hustle alive.**")
    except:
        st.markdown("**Vicky:** Uh-oh, that ticker ain't hittin’. Double check it for me.**")