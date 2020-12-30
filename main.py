#!python3
# Ａ simple script to retrieve the q skill name of any champ for any patch version
# Uncomment the inputs to input interactively
import requests

# PATCH_VERSION = input("Enter patch version ")
PATCH_VERSION = "8.2.1"
# versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
# CHAMPION_NAME = input("Enter champion name")
CHAMPION_NAME = "Aatrox"

url = "http://ddragon.leagueoflegends.com/cdn/" + PATCH_VERSION + "/data/en_US/champion/" + CHAMPION_NAME + ".json"
response = requests.get(url)
response.raise_for_status()

raw_champion_json_data = response.json()
spells = raw_champion_json_data["data"][CHAMPION_NAME]["spells"]
q_spell = spells[0]
print("Q skill name for ", CHAMPION_NAME, " is ", q_spell["name"])
