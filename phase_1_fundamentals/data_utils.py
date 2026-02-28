import csv

def export_to_csv(filename, data, headers):
    """A reusable tool to convert a list of dicts to CSV"""
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    return f"Successfully exported to {filename}"


def import_from_csv(filename):
    """Reads a CSV and turns it back into a list of Python dictionaries"""
    data = []
    with open(filename, "r") as csvfile:
        # DictReader automatically uses the first row as the keys (headers)
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))          #We turn it into a standard dictionary
    return data