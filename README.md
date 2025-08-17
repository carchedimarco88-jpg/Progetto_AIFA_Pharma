# 💊 Progetto AIFA – Analisi del Consumo di Farmaci in Italia (dal 2016)

![Logo AIFA](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/AIFA_Logo.svg/800px-AIFA_Logo.svg.png)  
_Analisi clinica e visualizzazione dei dati farmaceutici pubblici tramite BigQuery e SQL_

---

## 🔍 Obiettivo del Progetto

Analizzare in modo strutturato i dati open pubblicati da AIFA relativi alla **spesa e consumo di farmaci** in Italia.  
L’obiettivo è identificare trend, anomalie, e differenze regionali per supportare decisioni cliniche, politiche sanitarie e studi accademici.

---

## 🧱 Fasi del Lavoro

### 1. **Download dei Dataset**
- Fonte: [Open Data AIFA](https://www.aifa.gov.it/web/guest/open-data)
- Periodo: dal 2016 al presente (aggiornabile annualmente)
- Tipologia: CSV, delimitatore `|`

### 2. **Pulizia e Unificazione**
- Conversione encoding UTF-8
- Uniformazione intestazioni e delimitatori
- Rimozione righe vuote e note a piè pagina

### 3. **Caricamento su BigQuery**
- Dataset: `farmaci_aifa`
- Tabelle: `DATASET_AIFA_CONSUMO_FARMACI_2016`, `..._2017`, `..._2023`
- Schema:  
  `anno`, `regione`, `atc1`, `descrizione_atc1`, `consumo_ddd`, `spesa_convenzionata`, `spesa_flusso_tracciabilita`, `numero_confezioni`

### 4. **Query SQL**
- **Query #1**: Totale spesa per anno, regione e ATC1  
  ```sql
  SELECT anno, regione, atc1, SUM(spesa_convenzionata + spesa_flusso_tracciabilita) AS spesa_totale
  FROM ...
  GROUP BY anno, regione, atc1
  ORDER BY spesa_totale DESC;

