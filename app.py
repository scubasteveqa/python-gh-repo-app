import requests
import streamlit as st

def get_weather_boston():
    url = "https://wttr.in/Boston?format=%C+%t+%h+%w"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None  # Return None if fetching weather data failed

st.title("Boston Weather Checker")

if st.button("Check Weather in Boston"):
    weather = get_weather_boston()
    st.write(f"Weather data response: {weather}")  # Add debug information
    if weather is not None:
        try:
            parts = weather.split()
            status = parts[0]  # The first part is the status
            temperature = parts[1][1:]  # Remove the "+" sign from temperature
            humidity = parts[2]
            wind = parts[3][1:]  # Remove the "←" sign from wind speed
            st.write(f"Weather in Boston:")
            st.write(f"Status: {status}")
            st.write(f"Temperature: {temperature} °F")
            st.write(f"Humidity: {humidity}")
            st.write(f"Wind: {wind} mph")
        except Exception as e:
            st.error(f"Failed to parse weather data: {e}")
    else:
        st.error("Failed to fetch weather data. Please try again later.")
