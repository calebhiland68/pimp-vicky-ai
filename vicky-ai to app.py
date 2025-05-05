import streamlit as st
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="Pimp Vicky AI", page_icon=":chart_with_upwards_trend:")

st.title("Pimp Vicky: Your Stock Assistant AI")

# Greeting
st.write("Hey, I'm Pimp Vicky. Let's make some money moves.")
st.write("I'll help you with stock predictions based on your strategy.")

# Step 1: Ask for stock symbol
stock = st.text_input("What stock are you looking at? (Use the stock symbol, e.g., AAPL for Apple)")

# Step 2: Ask for investment amount
amount = st.number_input("How much money do you want to invest?", min_value=1.0, step=1.0)

# Step 3: Ask for investment style
strategy = st.radio("How do you want to invest?", ("Day Trading", "Long Term"))

# Trigger analysis
if st.button("Run Prediction"):
    if stock:
        st.subheader(f"Analyzing {stock.upper()}...")
        ticker = yf.Ticker(stock)
        data = ticker.history(period="5d")

        if not data.empty:
            st.line_chart(data["Close"])
            current_price = data["Close"].iloc[-1]
            shares = round(amount / current_price, 2)

            if strategy == "Day Trading":
                st.write(f"Day Trading Strategy for {stock.upper()}:")
                st.write(f"With ${amount}, you could buy about {shares} shares at ${current_price:.2f} per share.")
                st.write("Tip: Watch for morning volatility and set a stop-loss.")
            else:
                st.write(f"Long Term Strategy for {stock.upper()}:")
                st.write(f"With ${amount}, you could invest in about {shares} shares.")
                st.write("Tip: Look at the 6-month and 1-year trends for better decisions.")

            st.success("Prediction complete. Come back tomorrow for fresh data!")
        else:
            st.error("Could not fetch data. Make sure the symbol is correct.")
    else:
        st.warning("Enter a stock symbol to get started.")