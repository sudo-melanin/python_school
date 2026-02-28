import csv

def generate_inventory_report(product_list, filename):
    filtered_product = [products for products in product_list if products["stock"] > 0]
    headers = ["item", "price", "stock"]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(filtered_product)

