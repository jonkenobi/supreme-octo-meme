#!python3
# Ａ simple script to retrieve the q skill name of any champ for any patch version
# Uncomment the inputs to input interactively
import requests

versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
response = requests.get(versions_url)
response.raise_for_status()
VALID_PATCH_VERSIONS = response.json()

PATCH_VERSION = ""
while PATCH_VERSION not in VALID_PATCH_VERSIONS:
    PATCH_VERSION = str(input("Enter valid patch version: ").strip())

CHAMPION_NAME = str(input("Enter champion name: ").strip())
# CHAMPION_NAME = "Aatrox"

url = "http://ddragon.leagueoflegends.com/cdn/" + PATCH_VERSION + "/data/en_US/champion/" + CHAMPION_NAME + ".json"
response = requests.get(url)
response.raise_for_status()

raw_champion_json_data = response.json()
spells = raw_champion_json_data["data"][CHAMPION_NAME]["spells"]
q_spell = spells[0]
print("Q skill name for ", CHAMPION_NAME, " at patch ", PATCH_VERSION, " is ", q_spell["name"])
