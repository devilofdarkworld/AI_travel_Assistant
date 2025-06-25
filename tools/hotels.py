# import streamlit as st
# import requests

# API_KEY = "887a0b2597msh1ac05f0cb070968p1daa8ajsncc524e764715"
# HEADERS = {
#     "X-RapidAPI-Key": API_KEY,
#     "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
# }

# def get_location_id(city):
#     url = "https://travel-advisor.p.rapidapi.com/locations/search"
#     params = {"query": city, "limit": "1", "lang": "en_US"}
#     response = requests.get(url, headers=HEADERS, params=params)
#     data = response.json()
#     if data.get("data"):
#         return data["data"][0]["result_object"]["location_id"]
#     return None

# def get_hotels(location_id):
#     url = "https://travel-advisor.p.rapidapi.com/hotels/list-by-latlng"
#     params = {
#         "latitude": "18.9388",  # Mumbai latitude
#         "longitude": "72.8354",  # Mumbai longitude
#         "limit": "6",
#         "currency": "USD",
#         "lang": "en_US"
#     }
#     response = requests.get(url, headers=HEADERS, params=params)
#     return response.json().get("data", [])

# # Streamlit UI
# st.title("🏨 Mumbai ya kisi jagah ke Hotels (Price + Photo)")

# city = st.text_input("Jagah ka Naam (e.g., Mumbai):")

# if city:
#     loc_id = get_location_id(city)
#     if loc_id:
#         hotels = get_hotels(loc_id)
#         if hotels:
#             for hotel in hotels:
#                 name = hotel.get("name")
#                 price = hotel.get("price")
#                 rating = hotel.get("rating")
#                 image = hotel.get("photo", {}).get("images", {}).get("medium", {}).get("url", "")
                
#                 if name:
#                     st.image(image, width=300)
#                     st.markdown(f"**{name}**")
#                     st.markdown(f"💲 Price: {price if price else 'N/A'}")
#                     st.markdown(f"⭐ Rating: {rating if rating else 'N/A'}")
#                     st.markdown("---")
#         else:
#             st.warning("Koi hotel data nahi mila.")
#     else:
#         st.error("Jagah ka Location ID nahi mila.")


import requests
from langchain.tools import tool
API_KEY = "887a0b2597msh1ac05f0cb070968p1daa8ajsncc524e764715"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
}
@tool
def get_hotels_for_city(city: str) -> dict:
    """
    Given a city name, fetch hotel data including name, price, rating, and image URL.
    Returns a structured dictionary with hotel details.
    """

    def get_location_id(city_name):
        url = "https://travel-advisor.p.rapidapi.com/locations/search"
        params = {"query": city_name, "limit": "1", "lang": "en_US"}
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json()
        if data.get("data"):
            return data["data"][0]["result_object"]["location_id"]
        return None

    def get_hotels_by_latlng(location_id, lat=18.9388, lng=72.8354, limit=6):
        url = "https://travel-advisor.p.rapidapi.com/hotels/list-by-latlng"
        params = {
            "latitude": str(lat),
            "longitude": str(lng),
            "limit": str(limit),
            "currency": "USD",
            "lang": "en_US"
        }
        response = requests.get(url, headers=HEADERS, params=params)
        return response.json().get("data", [])

    # --- Logic ---
    location_id = get_location_id(city)
    if not location_id:
        return {"error": f"Location ID not found for city '{city}'."}

    # Note: Hardcoded Mumbai lat/lng – can be improved using real city geolocation
    hotels_raw = get_hotels_by_latlng(location_id)
    
    hotels_cleaned = []
    for hotel in hotels_raw:
        name = hotel.get("name")
        price = hotel.get("price")
        rating = hotel.get("rating")
        image_url = hotel.get("photo", {}).get("images", {}).get("medium", {}).get("url", "")
        
        if name:
            hotels_cleaned.append({
                "name": name,
                "price": price or "N/A",
                "rating": rating or "N/A",
                "image": image_url or "N/A"
            })

    return {
        "city": city,
        "hotels_found": len(hotels_cleaned),
        "hotels": hotels_cleaned
    }
