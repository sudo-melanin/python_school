# Lists - ORDERED MUTABLE collections, mutable, defined using []

services = ["Auth", "Database", "Caching", "Logging"]

# Accessing by index: python starts at 0 (zero indexing)
print(f"Primary Service: {services[0]}")        # prints the first item
print(f"Last Service: {services[-1]}")          # prints the last item

## Adding and Removing
services.append("Email")                         # Adds to the end
services.insert(1, "Billing")                    # Adds to index 1
services.remove("Caching")                       # Removes by value

print(f"\nUpdated Services: {services}")

# slice - allows you to grab a sub section of a list, the syntax list[start:end]
# it includes at the 'start' and stop just before the 'end' index

mid_serivices = services[1:4]                   # slices from index 1 to index 3
print("\n",mid_serivices)                       
end_services = services[2: ]                    # slices from index 2 to the last item
print(end_services)
start_services = services[ : 2]                 # slices from the first index to the index before index 2
print(start_services)


# Dictionary - The MAPPING brick, uses a key - value pair, declared with {}
# defining a user profile
user_profile = {
    "user_id": "001",
    "username": "Aimz",
    "role": "Admin",
    "is_active": True
}

# Accessig data -   using the key
print(f"Current user: {user_profile['username']}")                      # prints the value for the 'username' key

# Adding/updating data
user_profile["last_login"] = "26-02-2026"                               # Adds a new key
user_profile["role"] = "Super_Admin"                                    # Updates a existing key

# .get() - if what you want access doesn't exist, it doesn't crash, it returns a default error
phone = user_profile.get("phone", "Member does not exist")
print(phone)
print(user_profile.get("address", "Does not exist"))

# Nested Challenge

server_data = {
    "server_name": "Main-Cluster",
    "stats": {
        "cpu_usage": 45,
        "memory_free": "2GB"
    }
}
print(server_data["stats"]["cpu_usage"])                            # returs 45


# Tuples - The IMMUTABLE brick, used for data that doesn't change, defined using ()
# Defining a Tuple
server_location = (6.553, 3.399)
# Accessing by index
print(f"Lattitude: {server_location[0]}")

#server_location[0] = 3.4544                        # This line of code will throw an error as tuples cannot be editted.

# Sets  - The UNIQUE UNORDERED Brick, declared using the {}, contains no duplicates

# 1. Defining a Set with duplicates
visitor_ips = {"192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1"}

# 2. Python automatically removes the duplicate "192.168.1.1"
print(f"Unique Visitors: {visitor_ips}")

# 3. Checking for a value (Very fast in Sets!)
if "10.0.0.1" in visitor_ips:
    print("User is already logged.")


