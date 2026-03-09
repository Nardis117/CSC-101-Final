import unittest
from data import PlaceAirQuality


class TestPlaceAirQuality(unittest.TestCase):

    def setUp(self):
        """Create a sample PlaceAirQuality object used for all tests."""
        self.place = PlaceAirQuality(
            1,
            "Test City",
            "city",
            [50, 60, 70, 80, 90, 100, 110],
            [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
            1000,
            {"cars": 5000, "power_plants": 3000, "industry": 2000, "deforestation": 0},
            {"solar": 30, "wind": 20, "hydro": 10, "coal": 20, "gas": 20},
            ["manufacturing"],
            ["Efficiency program"]
        )

    def test_calculate_aqi_average(self):
        result = self.place.calculate_aqi_average()
        self.assertEqual(result, 80)

    def test_calculate_pm25_average(self):
        result = self.place.calculate_pm25_average()
        self.assertEqual(result, 13)

    def test_find_aqi_extremes(self):
        highest, lowest = self.place.find_aqi_extremes()
        self.assertEqual(highest, 110)
        self.assertEqual(lowest, 50)

    def test_check_aqi_threshold(self):
        days = self.place.check_aqi_threshold(90)
        self.assertEqual(days, [6, 7])

    def test_total_emissions(self):
        total = self.place.total_emissions()
        self.assertEqual(total, 10000)

    def test_emissions_per_capita(self):
        per_capita = self.place.emissions_per_capita()
        self.assertEqual(per_capita, 10)

    def test_renewables(self):
        renewable_percent = self.place.renewables()
        self.assertEqual(renewable_percent, 60)


if __name__ == "__main__":
    unittest.main()
