import os

class NasaDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov"
        self.data_url = os.environ.get("NASA_DATA_URL", "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api")
        self.output_file = os.environ.get("OUTPUT_FILE", "nasadata.csv")
       