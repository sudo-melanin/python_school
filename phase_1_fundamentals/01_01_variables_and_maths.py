
# Assigning values
user_name = "Dev"           #string
user_age = 1                #int
is_active = True            #boolean
#status_code = 1             #int
api_version = 2.5           #float

# Checking the "DNA" of our variables
print(type(user_name))
print(type(user_age))
#print(type(status_code))
print(type(api_version))


result = 10 / 2
print(result)
print(type(result))

# Type casting
price_text = "19.99"
print(type(price_text))
price_number = float(price_text) # Now it's a float we can do math with
print(type(price_number))

total_logs = 27
remainder = total_logs % 5  # result is 2 - 

# f-strings (formatted strings): allows us plug variables directly inside a string
user_name = "Dev"
greeting = f"System alert: User {user_name} has {remainder} pending logs."
print(greeting)


# User input
#user_input = int(input("Enter a priority number: "))
#print(type(user_input))


# if/elif/else

status_code = int(input("Enter your status code: "))
priority_level = int(input("Enter your priority(1 - 5): "))
if  priority_level == 5 or status_code == 500:
    print("Critical: System will be down in 30seconds")
elif priority_level  > 3 or status_code != 200:
     print("Laying Brick: Log saved to database")
else:
    print("Log Skipped: Low Importance")


