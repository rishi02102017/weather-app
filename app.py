# import streamlit as st
# import requests

# st.set_page_config(page_title="Weather App 🌤️", layout="centered")

# st.title("🌦️ Weather Forecast App")
# st.markdown("Get real-time weather updates by entering a city, zip code, or coordinates.")

# # Info button for PM Accelerator
# with st.expander("ℹ️ About PM Accelerator"):
#     st.write("The Product Manager Accelerator is a learning platform that helps aspiring PMs gain real-world experience. [LinkedIn Page](https://www.linkedin.com/company/product-manager-accelerator/)")

# # User input
# location = st.text_input("Enter location (city, zip, etc.)")

# # OpenWeatherMap API
# API_KEY = "c3391e4bbe8586eabbd8576ae5cde133"  # Updated API key on Streamlit

# def get_weather(location):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     return response.json()

# if st.button("Get Weather"):
#     if not location:
#         st.error("Please enter a location.")
#     else:
#         data = get_weather(location)
#         if data.get("cod") != 200:
#             st.error(f"Error: {data.get('message')}")
#         else:
#             st.success(f"Weather for {data['name']}, {data['sys']['country']}")
#             st.metric("🌡️ Temperature", f"{data['main']['temp']} °C")
#             st.write("**Weather:**", data['weather'][0]['description'].title())
#             st.write("**Humidity:**", data['main']['humidity'], "%")
#             st.write("**Wind Speed:**", data['wind']['speed'], "m/s")


import streamlit as st
import requests
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# App Config
st.set_page_config(page_title="Weather App 🌤️", layout="centered")
st.title("🌦️ Weather + MongoDB CRUD App")
st.markdown("Search weather, save it, update or delete records.")

# About PM Accelerator
with st.expander("ℹ️ About PM Accelerator"):
    st.write("Product Manager Accelerator helps future PMs gain real-world skills. [LinkedIn Page](https://www.linkedin.com/company/product-manager-accelerator/)")

# MongoDB Connection
# MONGO_URI = "mongodb+srv://rishikashyap85p:Rishi%4012345@weather-app.1v8n4.mongodb.net/?retryWrites=true&w=majority&appName=weather-app"
# MONGO_URI = "mongodb+srv://rishikashyap85p:Rishi%4012345@weather-app.1v8n4.mongodb.net/?retryWrites=true&w=majority"
MONGO_URI = st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)
db = client.weather_db
collection = db.weather_records

# OpenWeatherMap API
API_KEY = "c3391e4bbe8586eabbd8576ae5cde133"

def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Input: Location
location = st.text_input("📍 Enter location (city name)")

col1, col2 = st.columns(2)
with col1:
    action = st.selectbox("Action", ["Get Weather", "Save", "View All", "Update", "Delete"])
with col2:
    record_id = st.text_input("ID to update/delete (for Update/Delete only)")

# Action Handler
if st.button("Run"):
    if action == "Get Weather":
        if not location:
            st.error("Enter a location.")
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
    
    elif action == "Save":
        if not location:
            st.warning("Please enter a location to save.")
        else:
            data = get_weather(location)
            if data.get("cod") == 200:
                entry = {
                    "location": location,
                    "temperature": data['main']['temp'],
                    "description": data['weather'][0]['description'],
                    "timestamp": datetime.now()
                }
                collection.insert_one(entry)
                st.success("✅ Weather record saved!")

    elif action == "View All":
        records = list(collection.find())
        if records:
            df = pd.DataFrame(records)
            df['_id'] = df['_id'].astype(str)
            st.dataframe(df)
        else:
            st.info("No records found.")

    elif action == "Update":
        if not record_id:
            st.warning("Enter a valid ID to update.")
        else:
            new_temp = st.number_input("New Temperature", value=0.0)
            result = collection.update_one(
                {"_id": record_id},
                {"$set": {"temperature": new_temp, "timestamp": datetime.now()}}
            )
            if result.modified_count:
                st.success("✅ Record updated.")
            else:
                st.error("No matching record found.")

    elif action == "Delete":
        if not record_id:
            st.warning("Enter a valid ID to delete.")
        else:
            result = collection.delete_one({"_id": record_id})
            if result.deleted_count:
                st.success("🗑️ Record deleted.")
            else:
                st.error("No matching record found.")

# --------------- BONUS FEATURES ------------------

st.subheader("📍 Google Maps View")
if location:
    map_query = location.replace(" ", "+")
    st.markdown(f"#### 📍 Map View for {location}")
    st.components.v1.iframe(
        f"https://maps.google.com/maps?q={map_query}&t=&z=13&ie=UTF8&iwloc=&output=embed",
        width=700,
        height=400,
    )

# st.subheader("🎥 YouTube Video About the City")
# yt_fallback = {
#     "Delhi": "https://www.youtube.com/embed/uN4WCEpYQTo",
#     "Mumbai": "https://www.youtube.com/embed/hLQtnzN1QkQ",
#     "New York": "https://www.youtube.com/embed/VpT_M1kWf-0",
#     "London": "https://www.youtube.com/embed/vEfRkD98FCk",
#     "Tokyo": "https://www.youtube.com/embed/CYGHxf_XjuA",
#     "Paris": "https://www.youtube.com/embed/6GV4N4wF7K8",
#     "Dubai": "https://www.youtube.com/embed/rRxW2a2GVlA",
#     "Singapore": "https://www.youtube.com/embed/iMiJFSK3xiE",
#     "Bangkok": "https://www.youtube.com/embed/TGm7skVOpNo",
#     "Sydney": "https://www.youtube.com/embed/ExQ2BL-LVKc"
# }
# yt_url = yt_fallback.get(location, "https://www.youtube.com/embed/dQw4w9WgXcQ")
# st.components.v1.iframe(yt_url, height=400)

st.subheader("📤 Export Saved Records")
export_option = st.selectbox("Choose export format", ["CSV", "JSON"])
if st.button("Export Now"):
    records = list(collection.find())
    if records:
        df = pd.DataFrame(records)
        df['_id'] = df['_id'].astype(str)
        if export_option == "CSV":
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "weather_data.csv", "text/csv")
        elif export_option == "JSON":
            st.download_button("Download JSON", df.to_json(orient="records", indent=2), "weather_data.json", "application/json")
    else:
        st.info("No records found to export.")

