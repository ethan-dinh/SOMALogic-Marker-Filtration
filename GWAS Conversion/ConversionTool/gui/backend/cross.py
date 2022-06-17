"""
Cross-Referencing to CSV
"""

# Importing Libraries
import pandas as pd
from typing import List
import csv

# Importing CSV File for UNIPROT IDs
def import_csv(filename) -> List:
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        ID = []
        for row in csv_reader:
            ID.append(row[0])
    return ID

# Pandas Processing
def pandas(uniprot):
    df = pd.read_csv("data.csv")
    custom_count = df[['UniProt ID', 'Count for Custom Panel']]
    custom_count = custom_count[~custom_count["Count for Custom Painel"].isnull()]
    
    list_all = df['UniProt ID'].tolist()
    list_custom = custom_count["UniProt ID"].tolist()
    output_custom = []
    output_all = []
    not_in = []

    for ID in uniprot:
        if ID not in list_custom:
            output_custom.append(ID)

    for ID in uniprot:
        if ID in list_all:
            output_all.append(ID)

    for ID in output_all:
        if ID not in list_custom:
            not_in.append(ID)
    
    print(len(output_custom))
    print(len(output_all))
    print(len(not_in))
    print(len(list_all))
    print(len(uniprot))

def main():
    uniprot = import_csv("UniprotIDs.csv") 
    pandas(uniprot)

if __name__ == "__main__":
    main()