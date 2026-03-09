class PlaceAirQuality:
    def __init__(self, place_id, place_name, place_type,
                 aqi_week, pm25_week, population,
                 emissions_sources, energy, income_sources,
                 sustainability_actions):
        self.place_id = place_id
        self.place_name = place_name
        self.place_type = place_type
        self.aqi_week = aqi_week
        self.pm25_week = pm25_week
        self.population = population
        self.emissions_sources = emissions_sources
        self.energy = energy
        self.sustainability_actions = sustainability_actions

    def __repr__(self):
        avg_aqi = self.calculate_aqi_average()
        avg_pm25 = self.calculate_pm25_average()
        return "PlaceAirQuality(name = {}, avg_aqi = {:.1f}".format(self.place_name, avg_aqi)
    #I'm not sure if we should have repr return all the values, add ones you think are important still

    def calculate_aqi_average(self):
        return sum(self.pm25_week) / len(self.pm25_week)

    def find_aqi_extremes(self):
        max_value = max(self.aqi_week)
        min_value = min(self.aqi_week)
        return [max_value, min_value]

    def check_aqi_threshold(self, threshold):
        days = []
        for i in range(len(self.aqi_week)):
            if self.aqi_week[i] > threshold:
                days.append(self.aqi_week[i])
        return days


    def total_emissions(self):
        total = 0
        for source in self.emissions_by_source:
            total += self.emissions_by_source[source]
        return total

    def emissions_per_capita(self):
        if self.population == 0:
            return 0
        return self.total_emissions() / self.population

    #def emission_sources?

    def renewables(self):
        renewable_types = ['solar', 'wind', 'hydro']
        renewable_total = 0
        total = 0

        for energy in self.energy_mix:
            total += self.energy_mix[energy]
            if energy in renewable_types:
                renewable_total += self.energy_mix[energy]

        if total == 0:
            return 0
        return (renewable_total / total) * 100


