"""
Testing for API communication
"""

# Importing Libraries
import requests

# Using requests to communicate to UNIProt API
api_url = "https://rest.uniprot.org/"
response = requests.get(api_url)
response.json()
