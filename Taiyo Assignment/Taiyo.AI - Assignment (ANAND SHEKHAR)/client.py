# client.py
import os
import logging
from scraper.nasa_scraper import NasaDataScraper

def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    configure_logging()
    os.environ["NASA_DATA_URL"] = "https://www.earthdata.nasa.gov/your-custom-data-url"
    os.environ["OUTPUT_FILE"] = "custom_output.csv"
    
    scraper = NasaDataScraper()
    scraper.run()
