# while loop, keeps on executing as long as the conditon is met.
# remember to always add a condition to stop the loop if you don't want an infinite loop.

is_running = True

while is_running:
    print("\n--- System Active ---")
    user_input = input("Enter 'q' to quit or any other key to stay online: ")
    
    if user_input.lower() == 'q':
        print("Shutting down...")
        is_running = False  # The condition becomes False, so the loop stops
    else:
        print("Still standing!")

# For loops - used to iterate over a known range of entities

# Simulating processing a batch of 5 logs
print("\n--- Starting Batch Process ---")

for i in range(1, 6): # This will count from 1 to 5
    print(f"Processing log number: {i}")

print("--- Batch Complete ---")

# Simulating 5 incoming logs with different status codes
log_codes = [200, 404, 0, 500, 999, 201]

print("--- Starting Batch Scan ---")

#CONTROLS

#continue -     Skips the rest of the current turn and jumps straight to the next one (the "Skip This One" button).
#break -        Exits the loop immediately (the "Emergency Stop" button)

for code in log_codes:
    if code == 0:
        print("Invalid log (Priority 0). Skipping...")
        continue  # Skips the rest of this turn and moves to the next code
    
    if code == 999:
        print("CRITICAL FAILURE (Code 999). Stopping all processes!")
        break  # Kills the loop entirely
        
    print(f"Processing Status Code: {code}")

print("--- Scan Finished ---")

while True:
    code = int(input("Enter a status code(999 to quit)"))
    if code == 0:
        print("Invalid code: try again")
        continue
    elif code == 999:
        print("Shutting down.......")
        break
    if code == 200:
        print("OK")
    elif code == 404:
        print("Not Found")
    elif code == 500:
        print("Critical")
    else:
        print("Invalid code:",code)