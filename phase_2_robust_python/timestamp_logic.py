from datetime import datetime

# 1. Capture the curret moment

now = datetime.now()

# 2. Create a 'safe' filename (No colon nor space as OS hates them in filenames)
# %Y = 2026, %m = 02, %d = 28, %H = Hour, %M = Minute, %S = Second

timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"rate_log_time_{timestamp}.json"

print(f"The system will save file to: {filename}")