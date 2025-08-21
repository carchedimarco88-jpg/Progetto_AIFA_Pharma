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
- R 

---

## Obiettivo del Progetto

Analizzare in modo strutturato i dati open pubblicati da AIFA relativi alla spesa e al consumo di farmaci in Italia.  
Individuare trend, anomalie e differenze regionali per supportare decisioni cliniche, politiche sanitarie e studi accademici.

---

## Fasi del Lavoro

### 1. Download dei dataset  
   - Fonte: [Open Data AIFA](https://www.aifa.gov.it/spesa-e-consumo-relativi-al-flusso-della-farmaceutica-convenzionata-e-degli-acquisti-diretti)  
   - Periodo: 2016–2023  
   - Formato: CSV (delimitatore `|`)



### 2. Pulizia e Unificazione automatizzata tramite script *Python* [`Extract_and_Summarize.py`](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/extract_and_summarize.py)

   Lo script esegue:
   - Uniformazione encoding e delimitatori
   - Rimozione righe vuote e note
   - Salvataggio dei file pronti per BigQuery 

### 3. Creazione del dataset su BigQuery
Il dataset è stato progettato e realizzato appositamente per questo studio, con l’obiettivo di garantire integrità, accessibilità e scalabilità nell’analisi dei dati AIFA.

   - Inizializzazione del progetto su Google Cloud Platform
   - Modellazione dello schema relazionale delle tabelle
   - Ingestione dei file CSV e normalizzazione dei dati
   - Validazione della coerenza semantica e sintattica
   - Pubblicazione del dataset su BigQuery: [DATASET_AIFA_CONSUMO_FARMACI_2016_2023](https://console.cloud.google.com/bigquery?hl=it&invt=Ab6BZg&project=primo-progetto-bigquery&ws=!1m4!1m3!3m2!1sanalisi-clinica-su-bigquery!2sDATASET_AIFA_CONSUMO_FARMACI_2016_2023)

     
### 4. Esportazione con SQL, trasformazione ed analisi in Excel  
Le query SQL eseguite su BigQuery hanno generato dataset strutturati, successivamente esportati in Excel per una fase di analisi preliminare e visualizzazione.

 - Pulizia finale dei dati e verifica della coerenza
 - Trasformazioni tabellari e analisi statistica con tabelle pivot
 - Costruzione di grafici statici e dashboard tematiche

### 5. Estrazione da PDF con Python
   - È stato sviluppato uno script Python per analizzare tabelle PDF (report AIFA) ed estrarre dati strutturati.
     ['compute_atc_variation.py'](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/compute_atc_variation.py)
     che automatizza l’analisi di un documento PDF.
   - I risultati sono stati confrontati e integrati con quelli ottenuti da Excel e BigQuery.

### 6. Modellazione predittiva e analisi avanzata con R È stata sviluppata una pipeline in R.
 - Pulizia e armonizzazione del dataset AIFA (2016–2023)
 - Analisi esplorativa dei trend di consumo per classe terapeutica e regione
 - Costruzione di modelli predittivi (Random Forest, ARIMA, Prophet) per stimare il consumo futuro
 - Valutazione delle performance dei modelli (RMSE, MAE)
 - Generazione di report automatici con RMarkdown e visualizzazioni interattive


## Query SQL

### Query #1 – Totale spesa per anno, regione e ATC1

La query completa è disponibile in  
[queries/Totale_spesa_per_anno_regione_codATCliv1.sql](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/queries/Totale_spesa_per_anno_regione_codATCliv1.sql)

---


## Analisi Variazione Categorie Farmaceutiche ATC Pre e Post COVID19

Questa sezione del progetto analizza la variazione di spesa farmaceutica per categoria ATC (livello 1) tra il periodo **Pre-COVID (2016–2019)** e **Post-COVID (2020–2023)**, a partire dal database ottenuto dalle tabelle open dell'AIFA.

### 📁 Struttura del progetto


---

## Sintesi Metodologica

I dati sono espressi come valori netti (al netto di pay-back, sconti e contributi) e non includono la spesa lorda iniziale.  
Per approfondimenti sui meccanismi di pay-back, sugli sconti convenzionali e sul calcolo dei valori netti vs. lordi, consulta il file [METODOLOGIA.md](./METODOLOGIA.md).

---

## Riferimenti

- AIFA Open Data: https://www.aifa.gov.it/content/open-data

- ## Dataset pubblico su BigQuery

Il dataset creato per lo studio co le tabelle AIFA è disponibile pubblicamente su BigQuery e contiene i dati AIFA sul consumo dei farmaci dal 2016 al 2023.

[Accedi al dataset su BigQuery](https://console.cloud.google.com/bigquery?hl=it&invt=Ab6BZg&project=primo-progetto-bigquery&ws=!1m4!1m3!3m2!1sanalisi-clinica-su-bigquery!2sDATASET_AIFA_CONSUMO_FARMACI_2016_2023)

Chiunque può:
- Visualizzare il dataset
- Eseguire query
- Scaricare i risultati

⚠️ Il dataset è in sola lettura: non è possibile modificarlo.## 📊 Dataset pubblico su BigQuery


- Monitoraggio Spesa Farmaceutica (PDF):  
  https://www.aifa.gov.it/documents/20142/241044/Monitoraggio_Spesa_gennaio-dicembre2016_agg.pdf  
