import yfinance as yf
import pandas as pd
import streamlit as st
import datetime

st.write("""
# Stock Price EDA

This will show the Stock Price History.

""")

ticker_symbol = "GOOGL"
current_date = datetime.datetime.now()
current_date_str = f"{current_date.year}-{current_date.month}-{current_date.day}"
ticker_data = yf.Ticker(ticker_symbol)
# ticker_df = ticker_data.history(period="1d", start="2010-05-31", end="2020-05-31")
ticker_df = ticker_data.history(period="1d", start="2010-05-31", end=current_date_str)

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)