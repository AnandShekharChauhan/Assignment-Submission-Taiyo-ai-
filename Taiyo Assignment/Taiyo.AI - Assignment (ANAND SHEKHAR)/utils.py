import csv

def save_to_csv(output_file, dataset_metadata):
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Title", "Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dataset_metadata)
        print("Data saved to", output_file)
