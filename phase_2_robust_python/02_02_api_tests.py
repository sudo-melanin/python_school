import requests

# Handshake with the GitHub server
response = requests.get("https://api.github.com")

# Note: response.status_code == 200 means success.
data = response.json()

# Discovery: Use .keys() to see what the server sent back before trying to access it
# print(data.keys())

# Safe Access: Fetching the URL without risking a KeyError crash
print(f"The Github API Documentation is at: {data.get('documentation_url', 'No result found')}")