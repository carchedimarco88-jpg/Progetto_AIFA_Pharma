# Analisi del Consumo di Farmaci in Italia

## **Analisi clinica e visualizzazione dei dati farmaceutici pubblici**  
_Dott. Carchedi Foca R.M. – Farmacista & Data Analyst_  

<img src="https://www.aifa.gov.it/o/aifa-theme/images/aifa/AIFA2021_Col(LR).png"
     alt="Logo AIFA"
     width="150" />  
 
---

## Indice

1. [Tecnologie e Metodi](#tecnologie-e-metodi)  
2. [Obiettivo del Progetto](#obiettivo-del-progetto)  
3. [Fasi del Lavoro](#fasi-del-lavoro)  
4. [Query SQL](#query-sql)  
5. [Sintesi Metodologica](#sintesi-metodologica)  
6.  [Riferimenti](#riferimenti)  

---

## Tecnologie e Metodi
 
- BigQuery
- SQL
- Excel   
- Python  

---

## Obiettivo del Progetto

Analizzare in modo strutturato i dati open pubblicati da AIFA relativi alla spesa e al consumo di farmaci in Italia.  
Individuare trend, anomalie e differenze regionali per supportare decisioni cliniche, politiche sanitarie e studi accademici.

---

## Fasi del Lavoro

1. Download dei dataset  
   - Fonte: [Open Data AIFA](https://www.aifa.gov.it/spesa-e-consumo-relativi-al-flusso-della-farmaceutica-convenzionata-e-degli-acquisti-diretti)  
   - Periodo: 2016–2023  
   - Formato: CSV (delimitatore `|`)  

2. Pulizia e Unificazione  
   - Conversione in UTF-8  
   - Uniformazione intestazioni  
   - Rimozione righe vuote  

3. Caricamento su BigQuery  
   - Dataset: `analisi-clinica-su-bigquery.DATASET_AIFA_2016_2023`
     
4. Esportazione e analisi in Excel
   - Le query SQL hanno prodotto dataset esportati in Excel per analisi preliminari e visualizzazioni.

5. Estrazione da PDF con Python
   - È stato sviluppato uno script Python per analizzare tabelle PDF (report AIFA) ed estrarre dati strutturati.

6. Insight finali
   - I risultati sono stati confrontati e integrati con quelli ottenuti da Excel e BigQuery.

---

## Query SQL

### Query #1 – Totale spesa per anno, regione e ATC1

La query completa è disponibile in  
[queries/Totale_spesa_per_anno_regione_codATCliv1.sql](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/queries/Totale_spesa_per_anno_regione_codATCliv1.sql)

---


## Analisi Variazione Categorie Farmaceutiche ATC Pre e Post COVID19

Questa sezione del progetto analizza la variazione di spesa farmaceutica per categoria ATC (livello 1) tra il periodo **Pre-COVID (2016–2019)** e **Post-COVID (2020–2023)**, a partire da un report PDF dell'AIFA.

### 📁 Struttura del progetto


---

## Sintesi Metodologica

I dati sono espressi come valori netti (al netto di pay-back, sconti e contributi) e non includono la spesa lorda iniziale.  
Per approfondimenti sui meccanismi di pay-back, sugli sconti convenzionali e sul calcolo dei valori netti vs. lordi, consulta il file [METODOLOGIA.md](./METODOLOGIA.md).

---

## Riferimenti

- AIFA Open Data: https://www.aifa.gov.it/content/open-data  

- Monitoraggio Spesa Farmaceutica (PDF):  
  https://www.aifa.gov.it/documents/20142/241044/Monitoraggio_Spesa_gennaio-dicembre2016_agg.pdf  
