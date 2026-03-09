import data

def load_places_from_file(filename):
    places = []

    with open(filename, "r") as file_obj:
        lines = file_obj.readlines()

    for line in lines[1:]:
        parts = line.strip().split(",")

        place_id = int(parts[0])
        place_name = parts[1]
        place_type = parts[2]
        population = int(parts[3])

        aqi_week = [int(x) for x in parts[4:11]]
        pm25_week = [float(x) for x in parts[11:18]]

        emissions = {
            "cars": float(parts[18]),
            "power_plants": float(parts[19]),
            "industry": float(parts[20]),
            "deforestation": float(parts[21])
        }

        energy = {
            "solar": float(parts[22]),
            "wind": float(parts[23]),
            "hydro": float(parts[24]),
            "coal": float(parts[25]),
            "gas": float(parts[26])
        }

        place = data.PlaceAirQuality(
            place_id,
            place_name,
            place_type,
            aqi_week,
            pm25_week,
            population,
            emissions,
            energy,
            [],
            []
        )

        places.append(place)

    return places