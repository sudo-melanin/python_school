import requests
import json
from datetime import datetime

# CONFIGURATION
URL = "https://open.er-api.com/v6/latest/USD"
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"rate_{timestamp}.json"

try:
    # Requesting external data (The most common point of failure in backends)
    response = requests.get(URL)

    # Parsing the JSON 'box' into a Python Dictionary - Serialization
    data = response.json()

    #Metadata
    data['processed_at'] = timestamp
    data['source'] = "ExchangeRate-API"

    # SAFETY: Defaulting to {} prevents an AttributeError if 'rates' is missing.
    # This ensures the next .get() call doesn't crash the script.
    rates = data.get('rates', {}) 
    
    naira = rates.get('NGN', 'N/A')
    
except requests.exceptions.ConnectionError:
    # Network Protection: Catching internet/DNS failures
    print("No Internet connection")

except Exception as e:
    # Global Catch: Handling unexpected issues (Server errors, JSON parsing errors)
    print(f"An error occurred: {e}")

else:
    # Data Persistence: Save the successful response for offline use
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Success: 1 USD = {naira} NGN. Data logged to {filename}")