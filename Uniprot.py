"""
Generating a list of UNIPROT IDs from GENOME NAMES
"""

# Importing Libraries
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Importing CSV File for GENES
def import_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        genes = []
        for row in csv_reader:
            genes.append(row)

    return genes   

# Main Function --------------------------------
def main():
    filename = input("Filename:")
    gene_names = import_csv(filename)
    print(gene_names)

if __name__ == "__main__":
    main()