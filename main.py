import requests
import os
from dotenv import load_dotenv


class Dog:

    def __init__(self, image_id, image_url, breed_name, origin, life_span, temperament):

        self.image_id = image_id
        self.image_url = image_url
        self.breed_name = breed_name
        self.origin = origin
        self.life_span = life_span
        self.temperament = temperament

    def display_info(self):

        print("Dog Information")
        print("-------------------------")
        print("Image ID:", self.image_id)
        print("Image URL:", self.image_url)
        print("Breed:", self.breed_name)
        print("Origin:", self.origin)
        print("Life Span:", self.life_span)
        print("Temperament:", self.temperament)


load_dotenv()
api_key = os.getenv("DOG_API_KEY")
url = "https://api.thedogapi.com/v1/images/search"
headers = {
    "x-api-key": api_key
}
params = {
    "limit": 1,
    "include_breeds": 1
}

try:

    if not api_key:
        raise ValueError("API Key is missing. Check your .env file.")

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()
    data = response.json()
    if not data:
        print("No dog images found.")
    else:
        image_data = data[0]
        if image_data["breeds"]:
            breed_data = image_data["breeds"][0]
            breed_name = breed_data.get("name") or "Unknown"
            origin = breed_data.get("origin") or "Unknown"
            life_span = breed_data.get("life_span") or "Unknown"
            temperament = breed_data.get("temperament") or "Unknown"
        else:
            breed_name = "Unknown"
            origin = "Unknown"
            life_span = "Unknown"
            temperament = "Unknown"

        dog = Dog(
            image_data["id"],
            image_data["url"],
            breed_name,
            origin,
            life_span,
            temperament
        )

        dog.display_info()


except requests.exceptions.Timeout:
    print("Error: Request timed out.")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Connection Error:", e)

except (KeyError, TypeError, IndexError, ValueError) as e:
    print("Error processing API response:", e)

