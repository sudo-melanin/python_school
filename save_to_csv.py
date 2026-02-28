#csv converter boilerplate

import csv

def save_to_csv(input_data, output_file):
    """
    A universal boilerplate to convert a list of dictionaries to a CSV file.
    Automatically detects headers from the first dictionary in the list.
    """
    if not input_data:
        #print("No data provided to export.")
        raise ValueError("Input data file is missing")

    # Automatically extract fieldnames from the first dictionary
    # This makes it work for ANY data (users, inventory, weather, etc.)
    column_headers = input_data[0].keys()
    try:
        with open(output_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=column_headers)
            
            writer.writeheader()
            writer.writerows(input_data)
            
        print(f" Successfully exported data to: {output_file}")
    except FileNotFoundError:
      print("File path not found")
    except PermissionError:
        print("Please grant the accurate permission")
    except Exception as e:
        print("An error occured: ",e)
    finally:
       print("Exiting csv saver.......")

