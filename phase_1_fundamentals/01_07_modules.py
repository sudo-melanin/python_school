# Importing the module from the other file (data_utils)
from  data_utils import export_to_csv, import_from_csv

# JSON styled data to converted to csv
raw_api_data = [
    {"user_id": "001", "name": "Aimz", "status": "active"},
    {"user_id": "002", "name": "Nesto", "status": "away"}
]

# Using the imported module

message = export_to_csv("final_report.csv", raw_api_data, ["user_id", "name", "status"])
print(message)

# Importing to python dictionary
imported_users = import_from_csv("final_report.csv")

print("----Data Successfully Imported----")
print(imported_users)

for user in imported_users:
    print(f"Users:{user['name']} | Status: {user['status']}")
