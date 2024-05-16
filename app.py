import requests
import streamlit as st

def get_exchange_rate():
    base_currency = "USD"
    target_currency = "CAD"
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"][target_currency]
    else:
        return None

st.title("USD to CAD Exchange Rate Checker")

if st.button("Check Exchange Rate"):
    exchange_rate = get_exchange_rate()
    if exchange_rate is not None:
        st.write(f"Current exchange rate from USD to CAD: {exchange_rate}")
    else:
        st.error("Failed to fetch exchange rate data. Please try again later.")
