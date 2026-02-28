# The old way:

user_ids = [101, 102, 103]
formatted_ids = []

for uid in user_ids:
    formatted_ids.append(f"ID-{uid}")

print(formatted_ids)

# The List Comprehension way:

user_ids1 = [101, 102, 103]
formatted_ids1 = [f"ID-{uid}" for uid in user_ids1]
print(formatted_ids1)


# with filtering conditions:

latency = [15, 80, 120, 45, 200, 30]
filtered_latency = [time for time in latency if time > 100]
print(filtered_latency)

usernames = ["aimz", "nesto", "admin", "dev_user"]
new_names = [name.capitalize() for name in usernames if name != "admin"]
print(new_names)


# converting a list to dictionary

user_ids = [101, 102, 103, 104]

# {key: value for item in list}
user_status_map = {uid: "offline" for uid in user_ids}

print(user_status_map)


# Another example:
scores = [45, 88, 72, 91, 30]
passed_score = [passed for passed in scores if passed > 70]
print(passed_score)