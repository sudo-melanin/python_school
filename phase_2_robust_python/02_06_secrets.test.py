import os
from dotenv import load_dotenv

# 1. Load the variables from the .env file into the system environment
load_dotenv()

# 2. Access the variable using the built-in 'os' (Operating System) module
api_key = os.getenv("WEATHER_API_KEY")
provider = os.getenv("CURRENCY_PROVIDER")

print(f"Connecting to {provider}...")
print(f"Using Key: {api_key}")