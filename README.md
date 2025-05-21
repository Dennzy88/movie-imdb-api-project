# 🎬 Movie IMDb API Project

This Python project extends a local dataset of movies with additional data from the OMDb API (Open Movie Database).  
It integrates IMDb rating, actors, and vote count into the original dataset and exports the result as XML.

---

## 🧩 Features

- Reads a local CSV file with basic movie info  
- Calls OMDb API for each movie to fetch:  
  - IMDb rating  
  - Actors  
  - IMDb vote count  
- Handles API errors and missing data gracefully  
- Saves the extended dataset to `filmovi.xml`  
- Sorts and displays Top 10 movies by IMDb rating  

---

## 📁 File Structure

```
movie-imdb-api-project/
│
├── main.py           # Main script
├── movies.csv        # Input dataset
├── filmovi.xml       # Exported enriched data
├── config.json       # API key storage (excluded via .gitignore)
├── .gitignore        # Ignores config.json and other sensitive files
├── notes.txt         # Task summary and GitHub repo link
```

---

## 🔐 Security Notice

Please create a `config.json` file with your OMDb API key:

```json
{
  "api_key": "YOUR_OMDB_API_KEY"
}
```

**Do not share your key.**  
This file is excluded via `.gitignore`.

---

## ▶️ How to Run

1. Make sure you have Python 3.x installed  
2. Install required package:

```bash
pip install requests
```

3. Place `movies.csv` and `config.json` in the same directory  
4. Run the script:

```bash
python main.py
```

---

## 🏆 Top 10 IMDb Rated Movies

After running, the program will output the top 10 highest-rated films from the dataset.

---

## 📝 Author

Created by **Dennzy88** as part of the IT Academy course & personal learning journey.
