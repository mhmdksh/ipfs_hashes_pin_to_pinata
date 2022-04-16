# Import Libraries
import os
import json
import requests

# Define pinata Variables
pinata_key=''
pinata_secret_key=''
headers = {'pinata_api_key': pinata_key, 'pinata_secret_api_key': pinata_secret_key}
pinned_hashes_endpoint = "https://api.pinata.cloud/data/pinList?status=pinned"
pinning_endpoint = "https://api.pinata.cloud/pinning/pinByHash"

# Get List of Pinned Hashes From Pinata
pinata_urls_list=[]
print("Pinned Hashes in Pinata:")
pin_list_response = requests.get(url=pinned_hashes_endpoint, headers=headers).json()
for i in range(pin_list_response['count']):
    pinata_urls_list.append(pin_list_response["rows"][i]["ipfs_pin_hash"])
pinata_urls_list = (sorted(pinata_urls_list))
print(*(pinata_urls_list), sep="\n")


# Pin IPFS Hashes from your list to Pinata
# Add your hashes in the list here in a line by line format (Check the output of the previous function "print(*(pinata_urls_list), sep="\n")"")
hahes_to_pin=[]
for diff_hash in hahes_to_pin:
    diff_response = requests.post(url=pinning_endpoint, headers=headers, json={
    "hashToPin": diff_hash
    })
    print (diff_response.content)