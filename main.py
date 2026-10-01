import os
import pandas as pd

BASE = "https://raw.githubusercontent.com/Greco1899/scrape_ufc_stats/main/"
PASTA_DADOS = "dados/brutos"

os.makedirs(PASTA_DADOS, exist_ok=True)

# nome no repositório remoto -> nome do arquivo salvo localmente
ARQUIVOS = {
    "ufc_fight_results.csv": "ufc_fight_results.csv",
    "ufc_fight_stats.csv": "ufc_fight_stats.csv",
    "ufc_fighter_tott.csv": "ufc_fighter_stats.csv",
    "ufc_fighter_details.csv": "ufc_fighter_details.csv",
    "ufc_event_details.csv": "ufc_event_details.csv",
}

for nome_remoto, nome_local in ARQUIVOS.items():
    df = pd.read_csv(BASE + nome_remoto)
    df.to_csv(f"{PASTA_DADOS}/{nome_local}", index=False)
    print(f"Atualizado: {nome_local} ({len(df)} linhas)")

print("Dados atualizados.")