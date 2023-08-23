# scraper/test_nasa_scraper.py
import unittest
from nasa_scraper import NasaDataScraper

class TestNasaDataScraper(unittest.TestCase):
    def test_fetch_data(self):
        scraper = NasaDataScraper()
        data = scraper.fetch_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
