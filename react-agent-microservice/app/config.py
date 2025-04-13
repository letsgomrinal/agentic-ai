import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
YELP_API_KEY = os.getenv("YELP_API_KEY")