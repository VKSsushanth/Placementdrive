import pandas as pd
import datetime

# Sample dataset with electronic items
data = {
    "Item": ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Desktop", "Camera"],
    "Purchase Date": ["2021-08-17", "2022-01-10", "2020-05-22", "2019-12-11", "2023-03-01", "2021-04-15"],
    "Replacement Period (Years)": [3, 2, 4, 2, 5, 3],
    "Location": ["New York", "San Francisco", "Los Angeles", "New York", "San Francisco", "Los Angeles"]
}

# Convert the dataset into a pandas DataFrame
inventory_df = pd.DataFrame(data)

# Sample E-Waste Collection Points
collection_points = {
    "New York": "123 Recycle St, NY",
    "San Francisco": "456 Green Ave, SF",
    "Los Angeles": "789 Eco Blvd, LA",
}

def calculate_replacement_date(purchase_date, replacement_period_years):
    purchase_date_obj = datetime.datetime.strptime(purchase_date, "%Y-%m-%d")
    replacement_date_obj = purchase_date_obj + datetime.timedelta(days=replacement_period_years*365)
    return replacement_date_obj

def check_for_replacements(inventory_df):
    today = datetime.datetime.today()
    inventory_df['Replacement Date'] = inventory_df.apply(
        lambda row: calculate_replacement_date(row['Purchase Date'], row['Replacement Period (Years)']), axis=1)
    due_for_replacement = inventory_df[inventory_df['Replacement Date'] <= today]
    
    if due_for_replacement.empty:
        print("No items need replacement at this time.")
    else:
        print("Items that need replacement:")
        print(due_for_replacement[['Item', 'Purchase Date', 'Replacement Date']])

def suggest_collection_point(location):
    if location in collection_points:
        print(f"Nearest collection point in {location}: {collection_points[location]}")
    else:
        print(f"No collection point found in {location}")

def e_waste_impact_analysis(inventory_df):
    total_items = len(inventory_df)
    today = datetime.datetime.today()
    items_to_replace = len(inventory_df[inventory_df['Replacement Date'] <= today])
    print(f"Total items: {total_items}, Items to replace: {items_to_replace}")

# Main function
def main():
    user_location = input("Enter your location (e.g., 'New York'): ")
    
    print("\nChecking for items that need replacement...")
    check_for_replacements(inventory_df)
    
    print("\nSuggesting e-waste collection point...")
    suggest_collection_point(user_location)
    
    print("\nE-Waste Impact Analysis:")
    e_waste_impact_analysis(inventory_df)

if __name__ == "__main__":
    main()
