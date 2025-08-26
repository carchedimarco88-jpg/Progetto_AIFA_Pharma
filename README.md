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

Analisi clinica e visualizzazione dei dati farmaceutici pubblici AIFA per individuare trend, anomalie e previsioni di consumo a supporto di decisioni cliniche e politiche sanitarie.

## Indice

1. [Introduzione](#introduzione)  
2. [Domanda di ricerca](#domanda-di-ricerca)  
3. [Tecnologie e Metodi](#tecnologie-e-metodi)  
4. [Workflow](#workflow)  
5. [Risultati chiave](#risultati-chiave)  
6. [Accesso al dataset pubblico](#accesso-al-dataset-pubblico)  
7. [Report e visualizzazioni](#report-e-visualizzazioni)  
8. [Riferimenti](#riferimenti)  
9. [Autore](#autore)  

## Introduzione

Lo scopo di questo progetto è analizzare in modo strutturato gli Open Data AIFA relativi alla spesa e al consumo di farmaci in Italia tra il 2016 e il 2023. I risultati supportano:

- decisioni cliniche basate su evidenze di consumo  
- ottimizzazione della spesa pubblica  
- pianificazione delle risorse sanitarie  

## Domanda di ricerca

Quali classi di farmaci hanno mostrato variazioni significative di consumo dal 2016 al 2023 e come prevedere i trend futuri per guidare politiche sanitarie e approcci di medicina di precisione?

## Tecnologie e Metodi

| Strumento    | Utilizzo principale                                     |
|--------------|----------------------------------------------------------|
| BigQuery     | hosting e interrogazione del dataset AIFA                |
| SQL          | estrazione, aggregazione e preparazione dei dati         |
| Python       | pulizia automatizzata, estrazione dati da PDF            |
| Excel        | analisi preliminare, incrocio con dati ISTAT             |
| R            | modellazione predittiva e report automatici con RMarkdown |


Le principali fasi metodologiche sono:

- pulizia e armonizzazione dei CSV AIFA  
- creazione del dataset relazionale su BigQuery  
- normalizzazione pro capite con dati ISTAT  
- estrazione automatica di tabelle da PDF  
- modelli predittivi (Random Forest, ARIMA, Prophet)  
- validazione con RMSE e MAE  
- reportistica interattiva e statica  


## Workflow

1. Scaricare i CSV AIFA (2016–2023) dal portale Open Data AIFA.  
2. Pulizia e standardizzazione con `extract_and_summarize.py`.  
3. Creazione e pubblicazione del dataset in BigQuery.  
4. Esportazione dei risultati da BigQuery e analisi preliminare in Excel.  
5. Normalizzazione pro capite con dati ISTAT per regione e anno.  
6. Estrazione di tabelle da report PDF con `compute_atc_variation.py`.  
7. Costruzione e validazione di modelli predittivi in R (Random Forest, ARIMA, Prophet).  
8. Generazione di report automatici e dashboard interattive con RMarkdown.  

## Risultati chiave

- individuazione delle classi ATC con variazioni di consumo più marcate  
- previsioni di consumo per il triennio successivo  
- dashboard e report per stakeholder non tecnici  
- dataset AIFA 2016–2023 pubblicato su BigQuery  

## Accesso al dataset pubblico

Il dataset relazionale contenente i dati AIFA dal 2016 al 2023 è disponibile gratuitamente su BigQuery.  

Accedi qui:  
https://console.cloud.google.com/bigquery?hl=it&invt=Ab6BZg&project=primo-progetto-bigquery

## Report e visualizzazioni

- report interattivi e statici in HTML/PDF generati da `Analisi consumo farmaci.Rmd`  
- PDF per confronto Pre-COVID vs Post-COVID disponibili in `Report-Statici/`  

## Riferimenti

- AIFA Open Data: https://www.aifa.gov.it/open-data  
- Monitoraggio Spesa Farmaceutica AIFA:  
  https://www.aifa.gov.it/documents/20142/241044/Monitoraggio_Spesa_gennaio-dicembre2016_agg.pdf  
- ISTAT Popolazione residente: https://demo.istat.it/app/?i=POS  

## Autore

Foca Marco Carchedi  
Farmacista abilitato & Data Analyst  
carchedimarco88@gmail.com  















