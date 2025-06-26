# AI Travel Assistant

An intelligent, chat-based travel planner built with LangChain, Groq (LLaMA 3), and Streamlit. This application helps users plan trips by providing real-time weather data, information about local attractions, hotel suggestions, and destination images.

---

## Features

- Chat-based travel question and answer system  
- Step-by-step itinerary planning  
- Real-time weather updates  
- Discovery of attractions and landmarks  
- Hotel suggestions with related images  
- Destination image previews

---

## Tech Stack

- LangChain  
- Groq (LLaMA 3)  
- Streamlit  
- Open APIs (OpenWeather, Unsplash, Wikipedia, RapidAPI)

---

## Setup Instructions

### Python Environment

- Python version: 3.10.12

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/devilofdarkworld/travel-assistant-ai.git
   cd travel-assistant-ai

2.Install dependencies:

   `pip install -r requirements.txt

3.Copy the example environment file and update API keys:
   cp .env.example .env

4.Open .env and add your API keys:
   OPENWEATHER_API_KEY=your_openweather_api_key
   GROQ_API_KEY=your_groq_api_key
   UNSPLASH_ACCESS_KEY=your_unsplash_access_key

5.Run the Application   
streamlit run app.py

