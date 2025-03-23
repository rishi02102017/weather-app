# 🌦️ Weather Forecast App with MongoDB (Full CRUD + API Integrations)

This project was developed as part of the **AI Engineer Intern Technical Assessment** (AI/ML/GenAI Application). It includes a **full-stack weather app** with real-time API integration, MongoDB persistence, Google Maps embedding, and export options.

---

## 🚀 Features Implemented

### ✅ Tech Assessment 1 – Basic Weather App

- 📍 **User Input:** Enter any city name to fetch real-time weather
- 🌐 **Live Weather Data:** Uses OpenWeatherMap API (no static data)
- 🧊 **Details:** Temperature, Weather Description, Humidity, Wind Speed
- 📅 **5-Day Forecast:** Clean daily summary using `/forecast` API
- 📍 **Use My Location:** Auto-detects location via IP (with fallback)
- 🗺️ **Google Maps Embed:** Visual map view of the searched city
- 📤 **Streamlit UI:** Clean layout with icons and sections

---

### ✅ Tech Assessment 2 – Advanced Functionality

#### ✅ MongoDB + CRUD (MongoDB Atlas, NoSQL)
- **CREATE**: Save weather data with location and timestamp
- **READ**: View all saved weather records
- **UPDATE**: Modify temperature data via record ID
- **DELETE**: Delete records using ID
- ⚠️ All input validated for correctness

#### ✅ Export Functionality
- Export saved records as **CSV** or **JSON**

#### ✅ Google Maps Integration
- Dynamically displays embedded maps for the searched location

---

## ❌ Drawbacks / Limitations

### ⚠️ YouTube Integration Skipped
- We initially attempted embedding travel/weather videos via YouTube API. However:

- YouTube Data API **requires billing**, even for free quota
- Google Cloud billing setup is not feasible in the current scope
- Many videos were also region-blocked or unavailable in embeds

➡️ **Removed from final app** to ensure clean, error-free UI.

### ⚠️ IP-Based Location Accuracy
We use `geocoder.ip('me')` to fetch the user's current city. But this method has limitations:

| Issue | Explanation |
|-------|-------------|
| 🌍 Uses global IP routing | IP may route via different country (e.g. US server) |
| 🌐 VPN/ISP effects | May show incorrect region |
| 🔁 Accuracy varies | Especially in India, mobile/VPN setups |

#### ✅ Workaround / Solution
| Option | Accuracy | Status |
|--------|----------|--------|
| Browser Geolocation | 🔥 Best (GPS-level) | ❌ Not supported in Streamlit |
| Manual input (city) | ✅ Good fallback | ✅ Already implemented |
| Hybrid model | ✅ Best UX | ✅ Already done |

➡️ Final app allows both: **manual city input** + optional **auto-location**.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: OpenWeatherMap API, MongoDB Atlas
- **Database**: MongoDB (NoSQL)
- **Visualization**: Streamlit widgets, metrics, and Google Maps embed
- **Deployment**: Streamlit Cloud

---

## 🧪 How to Run

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Add Mongo URI in `.streamlit/secrets.toml`**  
```toml
MONGO_URI = "your_mongo_connection_string"
```

4. **Run the app**  
```bash
streamlit run app.py
```

---

## 🎥 Demo Video
*Link: https://drive.google.com/file/d/1zScxBIQMhbmouIFS-BcTj417_sPGC7EX/view?usp=sharing*

---

## 👤 Developer

- **Name:** Jyotishman Das
- **For:** Product Manager Accelerator Internship Assessment  

---
