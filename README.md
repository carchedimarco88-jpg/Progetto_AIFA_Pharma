# Analisi del Consumo di Farmaci in Italia

## **Analisi clinica e visualizzazione dei dati farmaceutici pubblici**  
_Dott. Carchedi Foca R.M. – Farmacista Abilitato & Data Analyst_  

<div style="display: flex; gap: 30px; flex-wrap: wrap; padding: 20px;">
  <img src="https://www.aifa.gov.it/o/aifa-theme/images/aifa/AIFA2021_Col(LR).png" alt="AIFA" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" alt="SQL" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" alt="R" style="height: 60px;">

</div>

---

## Indice


1. [Introduzione](#introduzione)
   - [Domanda di ricerca](#domanda-di-ricerca)

2. [Tecnologie e Metodi](#Tecnologie-e-Metodi)
   - [Fasi del Lavoro](#Fasi-del-Lavoro)
   - [Query SQL](#Query-SQL)
   - [Dataset pubblico su BigQuery](Dataset-pubblico-su-BigQuery)
   - [Report Statici](Report-Statici)
   - [Report RMarkdown](Report-RMarkdown)
     
3. [Risultati e discussione](#Risultati-e-discussione)
   - [Fasi del Lavoro](#fasi-del-lavoro)
   - [Query SQL](#query-sql)
     
- [Conclusioni](Conclusioni)  
- [Riferimenti](#riferimenti)  

---



# Introduzione

Lo scopo del seguente progetto è stato di analizzare in modo strutturato gli Open Data dell'AIFA relativi alla spesa e al consumo di farmaci in Italia con l'obbiettivo di individuare e prevedere i trend, le anomalie e le differenze regionali per supportare decisioni cliniche, politiche sanitarie, ottimizzare la spesa sanitaria e migliorare la pianificazione delle risorse.

### Domanda di ricerca
Quali classi di farmaci mostrano un aumento significativo nel consumo tra il 2016 e il 2023, e come possiamo prevedere il consumo futuro per supportare decisioni di politica sanitaria e medicina di precisione.
Domanda:
Quantitativa (analisi e modelli)
Applicabile (politiche sanitarie)
Innovativa (collegamento alla medicina personalizzata)

---

# Tecnologie e Metodi
 
- BigQuery
- SQL
- Excel   
- Python
- R

## Sintesi Metodologica

 - Pulizia e armonizzazione del dataset AIFA atta a garantire coerenza e qualità dei dati per analisi affidabili.
 - Analisi esplorativa per classe terapeutica e regione che permette di evidenziare differenze territoriali e comportamenti prescrittivi, utile per politiche regionali.
 - Modelli predittivi (Random Forest, ARIMA, Prophet) che permettono di stimare il consumo futuro, anticipando fabbisogni e costi.
 - Metriche di performance (RMSE, MAE) che validano l’accuratezza dei modelli, rendendo lo studio robusto e replicabile.
 - Report automatici con RMarkdown e visualizzazioni interattive che rendono i risultati accessibili a stakeholder non tecnici quali dirigenti sanitari e policy maker.

### Nota sui costi calcolati
I dati sono espressi come valori netti (al netto di pay-back, sconti e contributi) e non includono la spesa lorda iniziale.  
Per approfondimenti sui meccanismi di pay-back, sugli sconti convenzionali e sul calcolo dei valori netti vs. lordi, è disponibile il file: [METODOLOGIA.md](./METODOLOGIA.md).

---

# Risultati e discussione

## Fasi del Lavoro

### 1. Download dei dataset  
   - Fonte: [Open Data AIFA](https://www.aifa.gov.it/spesa-e-consumo-relativi-al-flusso-della-farmaceutica-convenzionata-e-degli-acquisti-diretti)  
   - Periodo di riferimento: dal 2016 al 2023  
   - Formato: CSV


### 2. Pulizia e unificazione automatizzata tramite script *Python* [Extract_and_Summarize.py](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/extract_and_summarize.py)

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

Inoltre, i dataset ottenuti con SQL sono stati incrociati con gli Open Data dell’ISTAT relativi alla popolazione residente per ciascuna regione e anno (dal 2019 in poi). I file ISTAT, uno per anno, sono stati riunificati e incrociati manualmente in Excel con i dati AIFA, al fine di calcolare il consumo pro capite per regione e anno. Questa metrica ha permesso di normalizzare i dati di consumo, rendendo possibile un confronto più equo tra territori con diversa densità abitativa.

### 5. Estrazione da PDF con Python
   - È stato sviluppato uno script Python ['compute_atc_variation.py'](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/compute_atc_variation.py) che automatizza l’analisi di un documento PDF per analizzare le tabelle (report AIFA ottenuti precedentemente con Excel) ed estrarre dati strutturati.
   - I risultati sono stati confrontati e integrati con quelli ottenuti da Excel e BigQuery.

### 6. Modellazione predittiva e analisi avanzata con R attraverso lo sviluppo di una pipeline.
 - Pulizia e armonizzazione del dataset AIFA (2016–2023)
 - Analisi esplorativa dei trend di consumo per classe terapeutica e regione
 - Costruzione di modelli predittivi (Random Forest, ARIMA, Prophet) per stimare il consumo futuro
 - Valutazione delle performance dei modelli (RMSE, MAE)
 - Generazione di report automatici con RMarkdown [`analisi_farmaci.Rmd`](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/reports/Analisi%20consumo%20farmaci.rmd) e visualizzazioni interattive


## Query SQL

### Query #1 – Totale spesa per anno, regione e categoria ATC lv.1

La query completa è disponibile in  
[queries/Totale_spesa_per_anno_regione_codATCliv1.sql](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/queries/Totale_spesa_per_anno_regione_codATCliv1.sql)

---

- ## Dataset pubblico su BigQuery

Il dataset creato per lo studio con le tabelle AIFA è disponibile pubblicamente su BigQuery e contiene i dati AIFA sul consumo dei farmaci dal 2016 al 2023.

[Accedi al dataset su BigQuery](https://console.cloud.google.com/bigquery?hl=it&invt=Ab6BZg&project=primo-progetto-bigquery&ws=!1m4!1m3!3m2!1sanalisi-clinica-su-bigquery!2sDATASET_AIFA_CONSUMO_FARMACI_2016_2023)

Chiunque può:
- Visualizzare il dataset
- Eseguire query
- Scaricare i risultati

Il dataset è in sola lettura: non è possibile modificarlo.

---

## Report Statici

### Analisi Variazione Categorie Farmaceutiche ATC Pre e Post COVID19
Questa sezione del progetto analizza la variazione di spesa farmaceutica per categoria ATC (livello 1) tra il periodo **Pre-COVID (2016–2019)** e **Post-COVID (2020–2023)**, a partire dal database ottenuto dalle tabelle open dell'AIFA.

---

## Report RMarkdown

Il file [`analisi_farmaci.Rmd`](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/reports/Analisi%20consumo%20farmaci.rmd) contiene:
- Pulizia e aggregazione del dataset AIFA (2016–2023)
- Analisi dei trend per classe ATC
- Modellazione predittiva con Random Forest
- Visualizzazioni e confronto tra valori reali e stimati
- Discussione, limiti e proposte future

Può essere compilato in HTML o PDF direttamente da RStudio.

---

## Conclusioni

---

## Riferimenti

- AIFA: [AIFA Open Data](https://www.aifa.gov.it/open-data)

- AIFA: [Monitoraggio Spesa Farmaceutica](https://www.aifa.gov.it/documents/20142/241044/Monitoraggio_Spesa_gennaio-dicembre2016_agg.pdf)

- ISTAT: [Open Data Popolazione Residente](https://demo.istat.it/app/?i=POS)
