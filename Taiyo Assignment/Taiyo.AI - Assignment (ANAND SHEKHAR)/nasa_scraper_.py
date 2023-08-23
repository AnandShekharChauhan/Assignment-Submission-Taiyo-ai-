# scraper/nasa_scraper.py
import os
import requests
from bs4 import BeautifulSoup
from .utils import save_to_csv
import logging

class NasaDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov"
        self.data_url = os.environ.get("NASA_DATA_URL", "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api")
        self.output_file = os.environ.get("OUTPUT_FILE", "nasadata.csv")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def fetch_data(self):
        try:
            response = requests.get(self.data_url)
            response.raise_for_status()
            self.logger.info("Data fetched successfully.")
            return response.content
        except requests.exceptions.RequestException as e:
            self.logger.error("Failed to fetch data: %s", e)
            return None

    def parse_data(self, data):
        soup = BeautifulSoup(data, "html.parser")
        dataset_links = soup.find_all("a", class_="title-link")
        dataset_metadata = []

        for link in dataset_links:
            title = link.text.strip()
            link_url = self.base_url + link.get("href")
            
            # Add metadata and values to the dataset
            dataset_metadata.append({"Title": title, "Link": link_url})
            
            # Fetch detailed data for each dataset here if needed
            
        return dataset_metadata

    def run(self):
        data = self.fetch_data()
        if data:
            dataset_metadata = self.parse_data(data)
            save_to_csv(self.output_file, dataset_metadata)
        else:
            self.logger.warning("No data to process.")
