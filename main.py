import data
import file_read
import sys

#Jake Carreon

def sustainability_message(place):
    """Return a short sustainability message based on the place data."""
    per_capita = place.emissions_per_capita()
    renewable_pct = place.renewables()

    if per_capita > 20:
        return "High emissions per person. This place should focus on cleaner transportation, energy efficiency, and lower fossil fuel use."
    if renewable_pct >= 50:
        return "Strong renewable energy share. This place should keep expanding clean energy and protecting air quality gains."
    return "Air quality and emissions still need improvement here. Expanding sustainable energy and cutting pollution from major sources should be a priority."


def load_places():
    """Load air quality data from a text file using exception handling."""
    try:
        places = file_read.load_places_from_file("air_quality_data.txt")
        return places
    except FileNotFoundError:
        print("Error: air_quality_data.txt was not found.")
        return []


def main():
    places = load_places()

    if len(places) == 0:
        print("No air quality data was loaded, so no calculations can be made.")
        return

    average_aqi_by_place = {}
    emissions_per_capita_by_place = {}

    total_aqi_sum = 0
    total_pm25_sum = 0
    total_place_count = 0

    for place in places:
        avg_aqi = place.calculate_aqi_average()
        avg_pm25 = place.calculate_pm25_average()
        aqi_extremes = place.find_aqi_extremes()
        threshold_days = place.check_aqi_threshold(100)
        total_emissions = place.total_emissions()
        per_capita = place.emissions_per_capita()
        renewable_pct = place.renewables()

        average_aqi_by_place[place.place_name] = round(avg_aqi, 1)
        emissions_per_capita_by_place[place.place_name] = round(per_capita, 4)

        total_aqi_sum += avg_aqi
        total_pm25_sum += avg_pm25
        total_place_count += 1

        print(place.place_name + ":")
        print("Average AQI:", round(avg_aqi, 1))
        print("Average PM2.5:", round(avg_pm25, 1))
        print("Highest AQI:", aqi_extremes[0])
        print("Lowest AQI:", aqi_extremes[1])
        print("Days Exceeding AQI 100:", threshold_days)
        print("Total Emissions:", round(total_emissions, 2))
        print("Emissions Per Capita:", round(per_capita, 4))
        print("Renewable Energy Share:", round(renewable_pct, 1), "%")
        print("Sustainability Message:", sustainability_message(place))
        print()

    overall_avg_aqi = total_aqi_sum / total_place_count
    overall_avg_pm25 = total_pm25_sum / total_place_count

    print("Overall Average AQI:", round(overall_avg_aqi, 1))
    print("Overall Average PM2.5:", round(overall_avg_pm25, 1))
    print("Average AQI by Place:", average_aqi_by_place)
    print("Emissions Per Capita by Place:", emissions_per_capita_by_place)


if __name__ == "__main__":
    main()
