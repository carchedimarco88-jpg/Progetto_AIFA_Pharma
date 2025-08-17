
# Analisi del Consumo di Farmaci in Italia   
  <span style="font-size: 28px;"> <b>Analisi clinica e visualizzazione dei dati farmaceutici pubblici</b> </span><br>
  <em style="font-size: 30px;">Dott. Carchedi Foca R.M. – Farmacista & Data Analyst </em>  💊💻📈
</p><img src="https://www.aifa.gov.it/o/aifa-theme/images/aifa/AIFA2021_Col(LR).png" width="150" alt="Logo AIFA"> <p align="center">

---
## 💻 Tecnologie e Metodi - Stack Analitico 🧰
<b>  SQL – BigQuery – Excel – Python – Power BI </b>

_Questo progetto si avvale di un ecosistema analitico integrato per l’elaborazione, visualizzazione e interpretazione dei dati farmaceutici pubblici._


## 🔍 Obiettivo del Progetto

Analizzare in modo strutturato i dati open pubblicati da AIFA relativi alla **spesa e consumo di farmaci** in Italia.  
L’obiettivo è identificare trend, anomalie, e differenze regionali per supportare decisioni cliniche, politiche sanitarie e studi accademici.

---

## 🧱 Fasi del Lavoro

### 1. **Download dei Dataset**
- Fonte: [Open Data AIFA](https://www.aifa.gov.it/spesa-e-consumo-relativi-al-flusso-della-farmaceutica-convenzionata-e-degli-acquisti-diretti)
- Periodo: dal 2016 al presente (aggiornabile annualmente)
- Tipologia: CSV, delimitatore `|`

### 2. **Pulizia e Unificazione**
- Conversione encoding UTF-8
- Uniformazione intestazioni e delimitatori
- Rimozione righe vuote e note a piè pagina

### 3. **Caricamento su BigQuery**
- Dataset: `analisi-clinica-su-bigquery.DATASET_AIFA_CONSUMO_FARMACI_2016_2023`
- Tabelle: `DATASET_AIFA_CONSUMO_FARMACI_2016`, `..._2017`, `..._2023`
- Schema:  
  `anno`, `regione`, `atc1`, `descrizione_atc1`, `consumo_ddd`, `spesa_convenzionata`, `spesa_flusso_tracciabilita`, `numero_confezioni`

### 4. **Query SQL**
- **Query #1**: Totale spesa per anno, regione e ATC1  
  ```sql
 
