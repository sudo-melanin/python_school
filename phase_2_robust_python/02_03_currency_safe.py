import requests
import json

try:
    # Requesting external data (The most common point of failure in backends)
    response = requests.get("https://open.er-api.com/v6/latest/USD")

    # Parsing the JSON 'box' into a Python Dictionary
    data = response.json()

    # SAFETY: Defaulting to {} prevents an AttributeError if 'rates' is missing.
    # This ensures the next .get() call doesn't crash the script.
    get_rates = data.get('rates', {}) 
    
    get_naira_value = get_rates.get('NGN', 'N/A')
    print(f"Current NGN Rate: {get_naira_value}")

except requests.exceptions.ConnectionError:
    # Network Protection: Catching internet/DNS failures
    print("No Internet connection")

except Exception as e:
    # Global Catch: Handling unexpected issues (Server errors, JSON parsing errors)
    print(f"An error occurred: {e}")

else:
    # Data Persistence: Save the successful response for offline use
    with open("todays_rate.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Rate successfully returned and saved to JSON")