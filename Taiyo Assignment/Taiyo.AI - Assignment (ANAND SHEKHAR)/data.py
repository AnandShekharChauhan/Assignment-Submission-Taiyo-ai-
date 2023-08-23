import requests
from bs4 import BeautifulSoup
import csv

class NasaDataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov"
        self.data_url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"
        self.output_file = "nasadata.csv"

    def fetch_data(self):
        response = requests.get(self.data_url)
        if response.status_code == 200:
            return response.content
        return None

    def parse_data(self, data):
        soup = BeautifulSoup(data, "html.parser")
        dataset_links = soup.find_all("a", class_="title-link")
        dataset_metadata = []

        for link in dataset_links:
            title = link.text.strip()
            link_url = self.base_url + link.get("href")
            dataset_metadata.append({"Title": title, "Link": link_url})

        return dataset_metadata

    def save_to_csv(self, dataset_metadata):
        with open(self.output_file, "w", newline="") as csvfile:
            fieldnames = ["Title", "Link"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset_metadata)

    def run(self):
        data = self.fetch_data()
        if data:
            dataset_metadata = self.parse_data(data)
            self.save_to_csv(dataset_metadata)
            print("Data saved to", self.output_file)
        else:
            print("Failed to fetch data.")

if __name__ == "__main__":
    scraper = NasaDataScraper()
    scraper.run()
