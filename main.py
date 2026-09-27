import pandas as pd

BASE = "https://raw.githubusercontent.com/Greco1899/scrape_ufc_stats/main/"

resultados = pd.read_csv(BASE + "ufc_fight_results.csv")