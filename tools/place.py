# import streamlit as st
# import requests

# # Your Unsplash Access Key
# UNSPLASH_ACCESS_KEY = 'hjjsm8v6IX7loTADYARD7bsLlZh8ezbX8bbfHsg4ntc'

# def get_images_for_place(place, count=6):
#     url = "https://api.unsplash.com/search/photos"
#     params = {
#         "query": place,
#         "client_id": UNSPLASH_ACCESS_KEY,
#         "per_page": count
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     images = [item["urls"]["regular"] for item in data.get("results", [])]
#     return images

# # Streamlit UI
# st.title("📍 Jagah ke Images Dekhein")

# place = st.text_input("Jagah ka Naam Likhiye:")

# if place:
#     st.subheader(f"🔍 '{place}' ke liye Images:")
#     images = get_images_for_place(place)
#     if images:
#         cols = st.columns(3)
#         for i, img_url in enumerate(images):
#             with cols[i % 3]:
#                 st.image(img_url, use_container_width=True)  # ✅ updated here
#     else:
#         st.warning("Koi images nahi mili, dusra naam try karein.")

# image_tool.py
from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os
load_dotenv()

UNSPLASH_ACCESS_KEY=os.getenv("UNSPLASH_ACCESS_KEY")

@tool
def get_images_for_place(place: str) -> str:
    """
    Fetch 6 Unsplash images for a given place name.
    Returns a newline-separated list of image URLs.
    """

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": place,
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 6
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"❌ Failed to fetch images for {place}. Status code: {response.status_code}"

    data = response.json()
    images = [item["urls"]["regular"] for item in data.get("results", [])]

    if not images:
        return f"❌ No images found for {place}."

    return f"🖼️ Top images for **{place}**:\n" + "\n".join(images)
