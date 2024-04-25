import json
import random
import csv
from faker import Faker

# PARAMETERS
NUMBER_OF_GENERATIONS = 100  # We drop duplicates at the end, we may end with less. Check console for actual number !
OUTPUT_FILE = "mock_data/property_with_scores.json"

# static vars
csv_file_path_codepostauxbelge = "mock_data/code-postaux-belge.csv"
csv_file_path_house_apartment = "mock_data/dataset_house_apartment.csv"


def readcsv(csvpath):
    with open(csvpath, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        data = []
        for row in csv_reader:
            data.append(row)
    return data


code_postaux_belge = readcsv(csv_file_path_codepostauxbelge)
house_apartment = readcsv(csv_file_path_house_apartment)

belgium_data = []

for row1 in code_postaux_belge:
    for row2 in house_apartment:
        if row1["locality"] == row2["locality"]:
            # If the 'id' matches, create a new dictionary with merged key-value pairs and append it to the results list
            belgium_data.append({**row1, **row2})


def drop_duplicates_by_lat_long(list_of_dicts):
    seen = set()
    result = []

    for d in list_of_dicts:
        key_tuple = (d["coordinates_latitude"], d["coordinates_longitude"])
        if key_tuple not in seen:
            result.append(d)
            seen.add(key_tuple)

    return result


def get_matching_color(matching_score):
    if matching_score < 14:
        return [195, 15, 17]
    elif matching_score < 28:
        return [232, 104, 0]
    elif matching_score < 42:
        return [252, 172, 19]
    elif matching_score < 56:
        return [242, 215, 5]
    elif matching_score < 70:
        return [194, 196, 0]
    elif matching_score < 84:
        return [80, 159, 52]
    else:
        return [12, 109, 35]


def get_ameneties(count):
    ameneties = [
        "Balcony or terrace",
        "Equipped kitchen",
        "bathroom with window",
        "Old building (until 1945)",
        "Bathroom with tub",
        "barrier-free",
        "Attic apartment",
        "Ground floor apartment",
        "Vacant / not rented",
        "becoming free",
        "Garage / parking space",
        "Garden",
        "basement, cellar",
        "furnished",
        "New building",
        "only new construction projects",
        "Passenger elevator",
        "renovated ",
        "senior-focused living",
        "Suitable for shared apartments"
    ]

    return [random.choice(ameneties) for _ in range(count)]


def generate_buy_row(belgium_data):
    current_pick = random.choice(belgium_data)
    fake_matching_percent = random.randint(0, 100)
    fake_matching_color = get_matching_color(fake_matching_percent)
    amenities = get_ameneties(random.choice([1, 2, 2, 3, 3, 4, 4, 5, 5]))
    missing_amenities = [x for x in get_ameneties(random.choice([0, 0, 0, 1, 1, 2, 2, 3])) if x not in amenities]

    return {
        "title": current_pick["subtype_of_property"] + " - " + current_pick["location"],
        "location": current_pick["location"],
        "type": current_pick["type_of_property"],
        "subtype": current_pick["subtype_of_property"],
        "rent_or_buy": "BUY",
        "coordinates_latitude": float(current_pick["latitude"]),
        "coordinates_longitude": float(current_pick["longitude"]),
        "surface_area": current_pick["house_area"],
        "price": current_pick["price"],
        "bedroom_count": current_pick["number_of_rooms"],
        "bathroom_count": random.randint(1, 2),
        "floor_count": random.randint(0, 2),
        "floor": random.randint(0, 5),
        "exposition": random.choice(
            ["south", "north", "east", "west", "north-east", "north-west", "south-west", "south-east"]),
        "construction_year": current_pick["construction_year"],
        "condition": random.choice(["EXCELLENT", "GOOD", "RENOVATED", "POOR", "STANDARD", "TO_RENOVATE"]),
        "ecoscore": random.choice(["A", "B", "C", "D", "E", "F"]),
        "has_terrace": random.choice([True, False]),
        "has_swimmingPool": random.choice([True, False]),
        "has_jacuzzi": random.choice([True, False]),
        "has_sauna": random.choice([True, False]),
        "matching_percent": str(fake_matching_percent),
        "matching_color": fake_matching_color,
        "matching_status": random.choice(["LIKED", "SUPERLIKED", "DISLIKED"]),
        "available_amenities": amenities,
        "missing_amenities": missing_amenities,
        "images": random.choice([[
            'https://ms.immowelt.org/16914243-54b5-4664-a0a0-b174ac47ed93/c331254e-2867-48e6-a175-fc0f59d9e6e7/original',
            'https://ms.immowelt.org/76882d6b-c395-4674-9a18-2ded140248ed/80b706b0-7615-40af-8987-5e4c33b82420/original',
            'https://ms.immowelt.org/e13b9c6b-2d4c-49a4-9454-63324163a4f7/5f6d918c-6f3e-470d-af9e-d2fc0e36c3d7/original'
        ], [
            'https://ms.immowelt.org/7cf572cc-501f-4ec4-9e2e-4c6808706319/6333f23f-7d4d-4ab6-bd6f-01f791007816/original',
            'https://ms.immowelt.org/a2408b83-9995-4c23-8d14-5d7aadac038f/3f2c84b3-97e1-4587-b02e-8e6c4a6187f1/original',
            'https://ms.immowelt.org/ee02219d-69c5-4ac8-a200-27c708833357/6a340461-5609-4a60-bb0d-c46356f91e51/original'
        ], [
            'https://ms.immowelt.org/4cd269ad-1cdb-48bb-8e7f-2ca33b768716/1a91f946-914a-4089-82b6-b589a7dcee4a/original',
            'https://ms.immowelt.org/e4510bca-83ff-480b-8209-784c33d3fdcf/b56adadb-4529-4a4e-8d99-6ba98412ed76/original',
            'https://ms.immowelt.org/b862ea44-ceba-4737-ba74-e2b9475a45cd/5cbcba7d-0d0b-40e7-9fa0-e4515318f903/original'
        ], [
            'https://ms.immowelt.org/780a216a-4bbe-48b1-b1ab-169a5baed10b/c5e6105d-152b-4c0d-852f-166f220dde91/original',
            'https://ms.immowelt.org/0dbe7e18-ab57-4d12-a968-754f091d1160/7bb4d72d-a2b6-40ea-aab5-290ee36db5b8/original',
            'https://ms.immowelt.org/5a767416-0297-45b2-a42b-5453f9338837/3c9b9a2d-15d8-4448-b6d5-cdbdfde09513/original'
        ]])
    }


def generate_rent_row(belgium_data):
    current_pick = random.choice(belgium_data)
    fake_matching_percent = random.randint(0, 100)
    fake_matching_color = get_matching_color(fake_matching_percent)
    amenities = get_ameneties(random.choice([1, 2, 2, 3, 3, 4, 4, 5, 5]))
    missing_amenities = [x for x in get_ameneties(random.choice([0, 0, 0, 1, 1, 2, 2, 3])) if x not in amenities]

    return {
        "title": current_pick["subtype_of_property"] + " - " + current_pick["location"],
        "location": current_pick["location"],
        "type": current_pick["type_of_property"],
        "subtype": current_pick["subtype_of_property"],
        "rent_or_buy": "RENT",
        "coordinates_latitude": float(current_pick["latitude"]),
        "coordinates_longitude": float(current_pick["longitude"]),
        "surface_area": current_pick["house_area"],
        "price": random.randint(500, 2000) // 50 * 50,
        "bedroom_count": current_pick["number_of_rooms"],
        "bathroom_count": random.randint(1, 2),
        "floor_count": random.randint(0, 2),
        "floor": random.randint(0, 5),
        "exposition": random.choice(
            ["south", "north", "east", "west", "north-east", "north-west", "south-west", "south-east"]),
        "construction_year": current_pick["construction_year"],
        "condition": random.choice(["EXCELLENT", "GOOD", "RENOVATED", "POOR", "STANDARD", "TO_RENOVATE"]),
        "ecoscore": random.choice(["A", "B", "C", "D", "E", "F"]),
        "has_terrace": random.choice([True, False]),
        "has_swimmingPool": random.choice([True, False]),
        "has_jacuzzi": random.choice([True, False]),
        "has_sauna": random.choice([True, False]),
        "matching_percent": str(fake_matching_percent),
        "matching_color": fake_matching_color,
        "matching_status": random.choice(["LIKED", "SUPERLIKED", "DISLIKED"]),
        "available_amenities": amenities,
        "missing_amenities": missing_amenities,
        "images": random.choice([[
            'https://ms.immowelt.org/16914243-54b5-4664-a0a0-b174ac47ed93/c331254e-2867-48e6-a175-fc0f59d9e6e7/original',
            'https://ms.immowelt.org/76882d6b-c395-4674-9a18-2ded140248ed/80b706b0-7615-40af-8987-5e4c33b82420/original',
            'https://ms.immowelt.org/e13b9c6b-2d4c-49a4-9454-63324163a4f7/5f6d918c-6f3e-470d-af9e-d2fc0e36c3d7/original'
        ], [
            'https://ms.immowelt.org/7cf572cc-501f-4ec4-9e2e-4c6808706319/6333f23f-7d4d-4ab6-bd6f-01f791007816/original',
            'https://ms.immowelt.org/a2408b83-9995-4c23-8d14-5d7aadac038f/3f2c84b3-97e1-4587-b02e-8e6c4a6187f1/original',
            'https://ms.immowelt.org/ee02219d-69c5-4ac8-a200-27c708833357/6a340461-5609-4a60-bb0d-c46356f91e51/original'
        ], [
            'https://ms.immowelt.org/4cd269ad-1cdb-48bb-8e7f-2ca33b768716/1a91f946-914a-4089-82b6-b589a7dcee4a/original',
            'https://ms.immowelt.org/e4510bca-83ff-480b-8209-784c33d3fdcf/b56adadb-4529-4a4e-8d99-6ba98412ed76/original',
            'https://ms.immowelt.org/b862ea44-ceba-4737-ba74-e2b9475a45cd/5cbcba7d-0d0b-40e7-9fa0-e4515318f903/original'
        ], [
            'https://ms.immowelt.org/780a216a-4bbe-48b1-b1ab-169a5baed10b/c5e6105d-152b-4c0d-852f-166f220dde91/original',
            'https://ms.immowelt.org/0dbe7e18-ab57-4d12-a968-754f091d1160/7bb4d72d-a2b6-40ea-aab5-290ee36db5b8/original',
            'https://ms.immowelt.org/5a767416-0297-45b2-a42b-5453f9338837/3c9b9a2d-15d8-4448-b6d5-cdbdfde09513/original'
        ]])
    }


output = []
for _ in range(NUMBER_OF_GENERATIONS):
    output.append(generate_buy_row(belgium_data))
    output.append(generate_rent_row(belgium_data))

final_output = drop_duplicates_by_lat_long(output)
with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(final_output, json_file, indent=4)

print(f"Generation done !\r\n'{OUTPUT_FILE}' updated with {len(final_output)} entries.")
