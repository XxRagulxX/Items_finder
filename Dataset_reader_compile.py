import json

# Load the data from a JSON file
input_filename = 'Fear.json'  # Replace this with your actual JSON file name

with open(input_filename, 'r') as json_file:
    data = json.load(json_file)

# Function to categorize items based on the title
def categorize_item(title):
    if "Preplanning" in title:
        return "Preplanning Assets"
    elif "asset" in title:
        return "Preplanning Assets"
    elif "Mask Mould" in title:
        return "Mask Mould"
    # elif "DLC" in title:
    #     return "DLC Pack"
    elif "Heist" in title:
        return "Heist Pack"
    elif "Weapon Pattern" in title:
        return "Weapon Patterns"
    elif "Weapon Sticker" in title:
        return "Weapon Stickers"
    elif "Weapon Pack" in title:
        return "Weapon Packs"
    elif "Tailor pack" in title:
        return "Tailor Packs"
    elif "Twitch" in title:
        return "Twitch Items"
    elif "Mask Pattern" in title:
        return "Mask Patterns"
    elif "Paint" in title:
        return "Spray Paints"
    elif "SprayCan" in title:
        return "Spray Paints"
    elif "Gloves" in title:
        return "Gloves Items"
    elif "Inventory Slot" in title:
        return "Inventory Slots"
    elif "Charm" in title:
        return "Weapon Charms"
    elif "Character" in title:
        return "Characters"
    # elif "Mask" in title:
    #     return "Masks"
    # Add more categories based on keywords as needed
    else:
        return "Other"

# Re-arrange the data
new_data = {}

# Iterate over each item and categorize based on title
for item in data['data']:
    category = categorize_item(item['title'])
    
    # Prepare the item structure
    new_item = {
        item['title']: {
            "itemId": item['itemId'],
            "price": item['regionData'][0]['price'],
            "discountedPrice": item['regionData'][0]['discountedPrice'],
            "currency": item['regionData'][0]['currencyCode']
        }
    }
    
    # Add the item to the relevant category
    if category not in new_data:
        new_data[category] = []
    new_data[category].append(new_item)

# Save the modified data to a new JSON file
output_filename = 'categorized_data.json'
with open(output_filename, 'w') as json_file:
    json.dump(new_data, json_file, indent=4)

print(f"Data has been categorized and saved to {output_filename}")
