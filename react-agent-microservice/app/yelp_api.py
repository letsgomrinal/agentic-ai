import os
import requests

YELP_API_KEY = os.getenv("YELP_API_KEY")

def search_restaurants(query, location="Vancouver", limit=5):
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"term": query, "location": location, "limit": limit}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    businesses = response.json()["businesses"]
    return [{"name": b["name"], "rating": b["rating"], "address": b["location"]["address1"]} for b in businesses]


#if __name__=="__main__":
#    query='best restaurants with ambience'
#    print(search_restaurants(query))