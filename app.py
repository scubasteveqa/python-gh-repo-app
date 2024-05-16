import requests
import streamlit as st

def get_weather_boston():
    url = "https://wttr.in/Boston?format=%C+%t+%h+%w"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch weather data"

st.title("Boston Weather Checker")

if st.button("Check Weather in Boston"):
    weather = get_weather_boston()
    if "Failed to fetch weather data" in weather:
        st.error(weather)
    else:
        status, temperature, humidity, wind = weather.split()
        st.write(f"Weather in Boston:")
        st.write(f"Status: {status}")
        st.write(f"Temperature: {temperature}")
        st.write(f"Humidity: {humidity}")
        st.write(f"Wind: {wind}")
