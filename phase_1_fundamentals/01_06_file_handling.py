# Use the 'with' keyword to open a file and work in, it closes the file automatcially.

# Writing to a file - 'w' - it overwrites everything on the file. 

with open("server-logs.txt", "w") as file:
    file.write("LOG Start: System Initializing.....\n")
    file.write("Status: All systems ready\n")
print("File created and written successfully")

# Appending to a file - 'a' - we use it to keep adding new lines to the bottome of a file.

with open("server-logs.txt", "a") as file:
    file.write("UPDATE: User 'Aimz' logged in.\n")
print("New Log Entry Added")

# Reading file content - 'r'

with open("server-logs.txt", "r") as file:
    content = file.read()
    print("Reading Server logs.....")
    print(content)

# writing from a list
new_users = ["Aimz", "Nesto", "Nas"]
with open("users_list.txt", "w") as file:
    for user in new_users:
        file.write(f"New user added: {user}\n")

print("All users added to the list")

# Reading back into a list
with open("users_list.txt", "r") as file:
    # .readlines() turns every line into a separate item in a list
    all_users = file.readlines()
    # .strip() cleans each line, note: the use of list comprehension.
    clean_users = [users.strip() for users in all_users ]       

print(f"Total Users in File: {len(all_users)}")
print(all_users)
print(clean_users)


# 'in' keyword - substring search in out files:

# Writing to the file - 'access_log.txt'
with open("access_log.txt", "w") as f:
    f.write("System Boot: 08:00\n")
    f.write("USER_LOGIN_FAILED: 08:10\n")
    f.write("ADMIN_ACCESS_GRANTED: 08:15\n")

# Reading the file
with open("access_log.txt", "r") as file:
    #Iterating over the lines in the file using the 'for' loop
    for line in file:
        # Using the conditional 'if' and the 'in' keyword to search for the substring in each line
        if "FAILED" in line:
            print(f"SECURITY ALERT!!! found in {line.strip()}")