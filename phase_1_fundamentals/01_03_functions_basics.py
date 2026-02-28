# A function is a reusable block of code
# it is defined using the 'def' keyword

def get_status_message (code):              #the parenthesis contains the parameters
    if code == 200:
        return "✅ OK: System Healthy"
    elif code == 404:
        return "ERROR: Resource Not Found"
    elif code == 500:
        return "CRITICAL: Server Failure"
    else:
        return "Unknown Status"
    

status_1 = get_status_message(200)
status_2 = get_status_message(500)

print(status_1)
print(status_2)

def calculate_uptime(days):
    return f"System has been up for {days} days"

current_uptime = calculate_uptime(20)
print(current_uptime)

# A function with a default parameter

def create_user_profile(username, age, role = "user"):
    return f"User: {username} (age: {age}) - Role: {role}"

user1 =  create_user_profile("Aimz", 33, "Admin")
user2 = create_user_profile("Nesto", 29)

print(user1)
print(user2)

# *args (arguments) - allows a function to take any number of positional values, turns them into a tuple.
def total_logs_processed (*count):
    return sum(count)

print(f"Total: {total_logs_processed(20,15,5,8,9)}")

# **kwargs (Keyword arguments) - Allows a function to take any number of extra key-value pair, it turns them into a dictionary.
def update_user_settings(user_id, **settings):
    return f"Updating User {user_id}, with {settings}"

print(update_user_settings("001", theme="dark", notification =True, language="EN" ))

#Exercise
def master_logger(message, **metadata):
    return f"ALERT: {message} - metadata: {metadata}"

print(master_logger("New update received", User="Aimz", role="Admin", verified=True, duration=1.5))
