import csv
import requests
import time
import xml.etree.ElementTree as ET
import json

# Ucitavanje API kljuca iz config.json
with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config["api_key"]
OMDB_URL = "http://www.omdbapi.com/"

# Ucitavanje filmova iz CSV fajla
filmovi = []
with open("movies.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    # Ciscenje BOM karaktera iz prve kolone ako postoji
    reader.fieldnames[0] = reader.fieldnames[0].lstrip('\ufeff')

    for row in reader:
        filmovi.append(row)

# Debugging: Print the contents of the filmovi list after loading the CSV
print("Loaded filmovi:", filmovi)

# Funkcija za dohvatanje podataka sa OMDb API
def dohvati_podatke(title, year):
    params = {
        "apikey": API_KEY,
        "t": title,
        "y": year
    }
    try:
        response = requests.get(OMDB_URL, params=params, timeout=5)
        data = response.json()
        # Debugging: Print the API response for each movie
        print(f"API Response for {title} ({year}):", data)
        if data.get("Response") == "True":
            return {
                "imdbRating": data.get("imdbRating", "N/A"),
                "actors": data.get("Actors", "N/A"),
                "imdbVotes": data.get("imdbVotes", "N/A")
            }
        else:
            return {"imdbRating": "N/A", "actors": "N/A", "imdbVotes": "N/A"}
    except Exception as e:
        print(f"Greska za '{title}': {e}")
        return {"imdbRating": "N/A", "actors": "N/A", "imdbVotes": "N/A"}

# Obrada filmova i dodavanje IMDb podataka
for film in filmovi:
    title = film.get("title", "Unknown Title")
    year = film.get("release_year", "Unknown Year")

    if title == "Unknown Title" or year == "Unknown Year":
        print("UPOZORENJE: Nedostaju kolone 'title' ili 'release_year' u nekom redu.")

    podaci = dohvati_podatke(title, year)
    film["imdbRating"] = podaci["imdbRating"]
    film["actors"] = podaci["actors"]
    film["imdbVotes"] = podaci["imdbVotes"]

    print(f"{title} ({year}) obradjen.")
    time.sleep(0.2)

# Snimanje rezultata u XML fajl
root = ET.Element("filmovi")
for film in filmovi:
    f = ET.SubElement(root, "film")
    for key, value in film.items():
        e = ET.SubElement(f, key)
        e.text = value

tree = ET.ElementTree(root)
tree.write("filmovi.xml", encoding="utf-8", xml_declaration=True)

# Prikaz 10 filmova sa najvisim IMDb ocenama
def ocena_vrednost(v):
    try:
        return float(v)
    except:
        return -1

filmovi_sortirani = sorted(filmovi, key=lambda x: ocena_vrednost(x["imdbRating"]), reverse=True)

print("\nTop 10 filmova po IMDb oceni:\n")
for film in filmovi_sortirani[:10]:
    print(f"{film.get('title', 'Unknown Title')} ({film.get('release_year', 'Unknown Year')}) - IMDb: {film.get('imdbRating', 'N/A')}")
