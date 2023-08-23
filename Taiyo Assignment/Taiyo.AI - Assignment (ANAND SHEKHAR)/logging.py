import logging

class NasaDataScraper:
    def __init__(self):
        # ...
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

    # ...
