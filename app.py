import datetime
import streamlit as st
from timezonefinder import TimezoneFinder

def get_current_time(city):
    # Map city names to their latitude and longitude coordinates
    city_coordinates = {
        "Boston": (42.3601, -71.0589),
        "London": (51.5074, -0.1278),
        "Perth": (-31.9505, 115.8605)
    }

    # Get the time zone for the specified city using timezonefinder
    tf = TimezoneFinder()
    city_timezone = tf.timezone_at(lat=city_coordinates[city][0], lng=city_coordinates[city][1])

    # Get the current time in the specified city
    city_time = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone(city_timezone))
    return city_time.strftime("%Y-%m-%d %H:%M:%S %Z")

st.title("Current Time in Different Cities")

selected_city = st.selectbox("Select a city:", ["Boston", "London", "Perth"])

if st.button("Get Current Time"):
    current_time = get_current_time(selected_city)
    st.write(f"Current time in {selected_city}: {current_time}")
