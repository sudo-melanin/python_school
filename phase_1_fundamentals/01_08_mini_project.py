from inventory_utils import generate_inventory_report

warehouse_data = [
    {"item": "rice", "price": 34.0, "stock": 5},
    {"item": "beans", "price": 38.0, "stock": 7},
    {"item": "yam", "price": 24.0, "stock": 0},
    {"item": "garri", "price": 12.0, "stock": 3}
]

generate_inventory_report(warehouse_data, "new_report.csv")

print("Report generated successfully")