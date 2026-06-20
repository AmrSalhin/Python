import requests
import streamlit as st

api_key = "Add_my_API_Key"
url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")
#call nasa api
response = requests.get(url)
#check response code
if response.status_code == 200:
    image_info = response.json()
    title = image_info["title"]
    img_url = image_info["hdurl"]
    description = image_info["explanation"]


    st.title(title)
    if img_url:
        response2 = requests.get(img_url)
        img_path = "img.png"
        with open(img_path, "wb") as f:
            f.write(response2.content)
        st.image(img_path)
    st.write(description)
else:
    st.error(f"Failed to fetch data from NASA. Status code: {response.status_code}")


