import streamlit as st
import requests

st.set_page_config(page_title="Weather App 🌤️", layout="centered")

st.title("🌦️ Weather Forecast App")
st.markdown("Get real-time weather updates by entering a city, zip code, or coordinates.")

# Info button for PM Accelerator
with st.expander("ℹ️ About PM Accelerator"):
    st.write("The Product Manager Accelerator is a learning platform that helps aspiring PMs gain real-world experience. [LinkedIn Page](https://www.linkedin.com/company/product-manager-accelerator/)")

# User input
location = st.text_input("Enter location (city, zip, etc.)")

# OpenWeatherMap API
API_KEY = "c3391e4bbe8586eabbd8576ae5cde133"  # Updated API key on Streamlit

def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

if st.button("Get Weather"):
    if not location:
        st.error("Please enter a location.")
    else:
        data = get_weather(location)
        if data.get("cod") != 200:
            st.error(f"Error: {data.get('message')}")
        else:
            st.success(f"Weather for {data['name']}, {data['sys']['country']}")
            st.metric("🌡️ Temperature", f"{data['main']['temp']} °C")
            st.write("**Weather:**", data['weather'][0]['description'].title())
            st.write("**Humidity:**", data['main']['humidity'], "%")
            st.write("**Wind Speed:**", data['wind']['speed'], "m/s")
