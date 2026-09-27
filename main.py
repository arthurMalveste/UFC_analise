import pandas as pd

BASE = "https://raw.githubusercontent.com/Greco1899/scrape_ufc_stats/main/"

resultados = pd.read_csv(BASE + "ufc_fight_results.csv")
ufc_fight_stats = pd.read_csv(BASE + "ufc_fight_stats.csv")
ufc_fighter_stats = pd.read_csv(BASE + "ufc_fighter_tott.csv")
ufc_fighter_details = pd.read_csv(BASE + "ufc_fighter_details.csv")
ufc_event_details = pd.read_csv(BASE + "ufc_event_details.csv")

resultados.to_csv("dados/brutos/ufc_fight_results.csv", index=False)
ufc_fight_stats.to_csv("dados/brutos/ufc_fight_stats.csv", index=False)
ufc_fighter_stats.to_csv("dados/brutos/ufc_fighter_stats.csv", index=False)
ufc_fighter_details.to_csv("dados/brutos/ufc_fighter_details.csv", index=False)
ufc_event_details.to_csv("dados/brutos/ufc_event_details.csv", index=False)

df = pd.read_csv("dados/brutos/ufc_fight_results.csv")

