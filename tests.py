import unittest
from data import PlaceAirQuality
import main
import file_read

#Ethan Huynh


test_place = PlaceAirQuality(1, 'Test City', 'city',
                             [50, 60, 70, 80, 90, 100, 110],
                             [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0],1000,
                             {"cars": 5000, 'power_plants': 3000, 'industry': 2000, "deforestation": 0},
                             {'solar': 30, 'wind': 20, 'hydro': 10, 'coal': 20, 'gas': 20},
                             ['manufacturing'])

class TestPlaceAirQuality(unittest.TestCase):

    place = test_place

    def test_repr(self):
        result = repr(self.place)
        self.assertIn("Test City", result)
        self.assertIn("80.0", result)

    def test_calculate_aqi_average_1(self):
        result = self.place.calculate_aqi_average()
        self.assertEqual(result, 80)

    def test_check_aqi_average_2(self):
        place = PlaceAirQuality(11, "Petra", 'city',
                                [10, 11, 12, 13, 14, 15, 16],[10.0] * 7,
                                10,{'cars': 10,
                                'power_plants': 10, 'industry': 10, 'deforestation': 10},
                                {'solar': 10, 'wind': 10, 'hydro': 10, 'coal': 10,
                                 'gas': 10},[])

        self.assertEqual(place.check_aqi_threshold(13), [5, 6, 7])

    def test_calculate_pm25_average_1(self):
        result = self.place.calculate_pm25_average()
        self.assertEqual(result, 13)

    def test_find_aqi_extremes_1(self):
        highest, lowest = self.place.find_aqi_extremes()
        self.assertEqual(highest, 110)
        self.assertEqual(lowest, 50)

    def test_find_aqi_extremes_2(self):
        place = PlaceAirQuality(30, 'Adiddas', 'city',
                                [10, 17, 10, 17, 10, 17, 10],[10.0] * 7,10,
                                {'cars': 10, 'power_plants': 10, 'industry': 10, 'deforestation': 10},
                                {'solar': 10, 'wind': 10, 'hydro': 10, 'coal': 10, 'gas': 10},
                                [])

        highest, lowest = place.find_aqi_extremes()
        self.assertEqual(highest, 17)
        self.assertEqual(lowest, 10)

    def test_check_aqi_threshold_1(self):
        days = self.place.check_aqi_threshold(90)
        self.assertEqual(days, [6, 7])

    def test_check_aqi_threshold_2(self):
        days = self.place.check_aqi_threshold(100)
        self.assertEqual(days, [7])

    def test_total_emissions_1(self):
        total = self.place.total_emissions()
        self.assertEqual(total, 10000)

    def test_total_emissions_2(self):
        place = PlaceAirQuality(8, '10', 'city',
                                [10, 10, 10, 10, 10, 10, 10],
                                [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],10,
                                {'cars': 10, 'power_plants': 10, 'industry': 10, 'deforestation': 10},
                                {'solar': 10, 'wind': 10, 'hydro': 10, 'coal': 10, 'gas': 10},
                                [])
        self.assertEqual(place.total_emissions(), 40)

    def test_emissions_per_capita_1(self):
        per_capita = self.place.emissions_per_capita()
        self.assertEqual(per_capita, 10)

    def test_emissions_per_capita_2(self):
        place = PlaceAirQuality(21, 'John', 'city', [10] * 7,
                                [10.0] * 7,10,{'cars': 10,
                                'power_plants': 11, 'industry': 12, 'deforestation': 13},
                                {'solar': 10, 'wind': 10, 'hydro': 10, 'coal': 10, 'gas': 10},
                                [])

        self.assertEqual(place.emissions_per_capita(), 4.6)

    def test_renewables(self):
        renewable_percent = self.place.renewables()
        self.assertEqual(renewable_percent, 60)

    def test_renewables_2(self):
        place = PlaceAirQuality(3, 'No Energy City',
                                'city', [10] * 7, [1] * 7,100,
                                {'cars': 100},{'solar': 0,
                                "wind": 0, "hydro": 0, 'coal': 0, 'gas': 0},
                                [])
        self.assertEqual(place.renewables(), 0)

class TestMain(unittest.TestCase):

    def test_main_1(self):
        tip = main.sustainability_message(test_place)
        self.assertIn('Strong renewable energy share', tip)

    def test_main_2(self):
        places = file_read.load_places_from_file("air_quality_data.txt")
        houston = places[1]
        tip = main.sustainability_message(houston)
        self.assertIn("High emissions per person", tip)

    def test_main_3(self):
        place = PlaceAirQuality(60, 'BAD', 'country',
                                [100] * 7, [100.0] * 7,100,
                                {'cars': 100, 'power_plants': 100,
                                 'industry': 100, 'deforestation': 100},
                                {'solar': 0, 'wind': 0, 'hydro': 0, 'coal': 100,
                                 'gas': 100},[])

        tip = main.sustainability_message(place)
        self.assertIn("still need improvement", tip)


class TestFileRead(unittest.TestCase):

    def test_file_read_1(self):
        places = file_read.load_places_from_file('air_quality_data.txt')
        self.assertEqual(len(places), 3)

    def test_file_read_2(self):
        places = file_read.load_places_from_file('air_quality_data.txt')
        self.assertEqual(places[1].place_name, 'Houston')

if __name__ == '__main__':
    unittest.main()
