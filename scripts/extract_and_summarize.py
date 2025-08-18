import camelot
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os


# Percorsi file
covid_pdf = os.path.join("reports", "CONFRONTO TRA SPESE FARMACEUTICHE PRE E POST COVID.pdf")
regioni_pdf = os.path.join("reports", "SPESA PRO CAPITE PER REGIONE.pdf")

# --- 1. Estrazione tabelle ---
print("📄 Leggo il PDF COVID...")
tables = camelot.read_pdf(covid_pdf, pages='1', flavor='lattice')
df_c = tables[0].df

# Pulizia: elimina colonne completamente vuote
df_c = df_c.dropna(how="all", axis=1)

# Debug: mostra dimensione e anteprima
print(f"➡️  Tabella COVID: {df_c.shape[1]} colonne trovate")
print(df_c.head())

# Rinomina colonne con nomi generici se necessario
df_c.columns = [f"Col_{i+1}" for i in range(df_c.shape[1])]

# --- 2. Salvataggio CSV ---
os.makedirs("data", exist_ok=True)
df_c.to_csv(os.path.join("data", "covid.csv"), index=False)

# --- 3. Grafico esempio (sostituisci con logica reale) ---
plt.figure(figsize=(8, 5))
df_c.iloc[1:, 1] = pd.to_numeric(df_c.iloc[1:, 1], errors='coerce')
df_c.plot(kind='bar', x=df_c.columns[0], y=df_c.columns[1])
plt.title("Esempio grafico spese COVID")
plt.savefig(os.path.join("outputs", "grafico_covid.png"))
plt.close()

# --- 4. PDF regioni ---
print("📄 Leggo il PDF REGIONI...")
tables_r = camelot.read_pdf(regioni_pdf, pages='1', flavor='lattice')
df_r = tables_r[0].df
df_r = df_r.dropna(how="all", axis=1)
print(f"➡️  Tabella REGIONI: {df_r.shape[1]} colonne trovate")
print(df_r.head())
df_r.columns = [f"Col_{i+1}" for i in range(df_r.shape[1])]
df_r.to_csv(os.path.join("data", "regioni.csv"), index=False)

# --- 5. Grafico regioni ---
plt.figure(figsize=(8, 5))
df_r.iloc[1:, 1] = pd.to_numeric(df_r.iloc[1:, 1], errors='coerce')
df_r.plot(kind='bar', x=df_r.columns[0], y=df_r.columns[1])
plt.title("Esempio grafico spesa pro capite")
plt.savefig(os.path.join("outputs", "grafico_regioni.png"))
plt.close()

# --- 6. Sintesi ---
with open(os.path.join("outputs", "SUMMARY.md"), "w", encoding="utf-8") as f:
    f.write("# Sintesi automatica\n\n")
    f.write(f"- Colonne tabella COVID: {df_c.shape[1]}\n")
    f.write(f"- Colonne tabella REGIONI: {df_r.shape[1]}\n")
    f.write("Grafici e CSV salvati in cartelle dedicate.\n")

print("✅ Elaborazione completata!")
