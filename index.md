<!--
Titolo: Analisi del Consumo Farmaci in Italia
Autore: dott. Foca Marco Carchedi
Data: 23 agosto 2025
Descrizione: Studio sull’andamento del consumo farmaceutico in Italia tra il 2016 e il 2023.
-->


# Analisi del Consumo di Farmaci in Italia

## **Analisi epidemiologica dei dati farmaceutici pubblici**  
 _Dott. Carchedi Foca R.M. – Farmacista Abilitato & Data Analyst_  

<div style="display: flex; gap: 30px; flex-wrap: wrap; padding: 20px;">
  <img src="https://www.aifa.gov.it/o/aifa-theme/images/aifa/AIFA2021_Col(LR).png" alt="AIFA" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" alt="SQL" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" style="height: 60px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" alt="R" style="height: 60px;">

</div>

---

## Indice del Progetto

### 1. [Introduzione](#introduzione)
   - [Domanda di ricerca](#domanda-di-ricerca)

### 2. [Tecnologie e Metodi](#Tecnologie-e-Metodi)
   - [Sintesi Metodologica](Sintesi-Metodologica)
   - [Fasi del Lavoro](#Fasi-del-Lavoro)
   
### 3. [Risultati e discussione](#Risultati-e-discussione)
   - [Fasi del Lavoro](#fasi-del-lavoro)
   - [Query SQL](#query-sql)
   - [Dataset pubblico su BigQuery](#Dataset-pubblico-su-BigQuery)
   - [Report Statici](#Report-Statici)
   - [Report RMarkdown](#Report-RMarkdown)
   - [Dashboard Interattiva](#Dashboard-Interattiva) con modello **Prophet**
   - [Verifica di coerenza](#Verifica-di-coerenza) (o validazione empirica)
     
### • [Conclusioni](Conclusioni)  

### • [Riferimenti](#riferimenti)  

---

<div class="info-links">
  <h4>* Documentazione</h4>
  <ul>
    <li>📄 <a href="https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/README.md" target="_blank">README del progetto</a></li>
    <li>🛡️ <a href="https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/LICENSE" target="_blank">Licenza</a></li>
  </ul>
</div>


---


# Introduzione

Lo scopo del seguente progetto è stato di analizzare in modo strutturato gli Open Data dell'AIFA relativi alla spesa e al consumo di farmaci in Italia con l'obbiettivo di individuare e prevedere i trend, le anomalie e le differenze regionali per supportare decisioni cliniche, politiche sanitarie, ottimizzare la spesa sanitaria e migliorare la pianificazione delle risorse.

![qualsiasi](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Screenshot%202025-08-23%20195157.png)
[Figura.1](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20VARIAZIONE%20CATEGORIE%20FARMACEUTICHE%20ATC%20PRE%20E%20POST%20COVID19.pdf) Classifica delle categorie farmaceutiche ATC in Italia in funzione della variazione di spesa nei periodi pre e post Covid-19.

### Domanda di ricerca
Quali classi di farmaci mostrano un aumento significativo nel consumo tra il 2016 e il 2023 e come possiamo prevedere il consumo futuro per supportare decisioni di politica sanitaria e medicina di precisione.

La domanda è:
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
Per approfondimenti sui meccanismi di pay-back, sugli sconti convenzionali e sul calcolo dei valori netti vs. lordi, è disponibile il file [Metodologia](./METODOLOGIA.md).

---

## Fasi del Lavoro

### 1. Download dei dataset  
   - Fonte: [Open Data AIFA](https://www.aifa.gov.it/spesa-e-consumo-relativi-al-flusso-della-farmaceutica-convenzionata-e-degli-acquisti-diretti)  
   - Periodo di riferimento: dal 2016 al 2023  
   - Formato: CSV


### 2. Pulizia e unificazione automatizzata tramite script *Python* 
Lo Script .py denominato [Extract and Summarize](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/extract_and_summarize.py) esegue:

   - Uniformazione encoding e delimitatori
   - Rimozione righe vuote e note
   - Salvataggio dei file pronti per BigQuery 

### 3. Creazione del dataset su BigQuery
Il dataset è stato progettato e realizzato appositamente per questo studio, con l’obiettivo di garantire integrità, accessibilità e scalabilità nell’analisi dei dati AIFA.

   - Inizializzazione del progetto su Google Cloud Platform
   - Modellazione dello schema relazionale delle tabelle
   - Caricamento dei file CSV e normalizzazione dei dati
   - Validazione della coerenza semantica e sintattica
   - Pubblicazione del dataset su BigQuery: [Dataset AIFA dal 2016 al 2023](https://console.cloud.google.com/bigquery?hl=it&invt=Ab6BZg&project=primo-progetto-bigquery&ws=!1m4!1m3!3m2!1sanalisi-clinica-su-bigquery!2sDATASET_AIFA_CONSUMO_FARMACI_2016_2023)

     
### 4. Esportazione con SQL, trasformazione ed analisi in Excel  
Le query SQL eseguite su BigQuery hanno generato dataset strutturati, successivamente esportati in Excel per una fase di analisi preliminare e visualizzazione.

 - Pulizia finale dei dati e verifica della coerenza
 - Trasformazioni tabellari e analisi statistica con tabelle pivot
 - Costruzione di grafici statici e dashboard tematiche

Inoltre, i dataset ottenuti con SQL sono stati incrociati con gli Open Data dell’ISTAT relativi alla popolazione residente per ciascuna regione e anno (dal 2019 in poi). I file ISTAT, uno per anno, sono stati riunificati e incrociati manualmente in Excel con i dati AIFA, al fine di calcolare il consumo pro capite per regione e anno. Questa metrica ha permesso di normalizzare i dati di consumo, rendendo possibile un confronto più equo tra territori con diversa densità abitativa.

### 5. Estrazione da PDF con Python
   - È stato sviluppato uno script Python denominato [Compute ATC Variation](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/scripts/compute_atc_variation.py) che automatizza l’analisi di un documento PDF per analizzare le tabelle (report AIFA ottenuti precedentemente con Excel) ed estrarre dati strutturati.
   - I risultati sono stati confrontati e integrati con quelli ottenuti da Excel e BigQuery.

### 6. Modellazione predittiva e analisi avanzata con R attraverso lo sviluppo di una pipeline.
 - Pulizia e armonizzazione del dataset AIFA (2016–2023)
 - Analisi esplorativa dei trend di consumo per classe terapeutica e regione
 - Costruzione di modelli predittivi (Random Forest, ARIMA, Prophet) per stimare il consumo futuro
 - Valutazione delle performance dei modelli (RMSE, MAE)
 - Generazione di report automatici con RMarkdown [Analisi spesa farmaceutica – RMarkdown](https://rpubs.com/CarchediFRM/1338164) e visualizzazioni interattive.

### 7. Pubblicazione della  [Dashboard Interattiva](https://carchedimarco88-jpg.github.io/Progetto_AIFA_Pharma/dashboard.html)

È stata creata una dashboard web interattiva che sintetizza i principali risultati dell’analisi, con visualizzazione dinamica dei trend temporali di consumo farmaci per regione e classe terapeutica. La dashboard è accessibile pubblicamente e consente l’esplorazione autonoma dei dati da parte di stakeholder e professionisti sanitari al seguente link [Dashboard Interattiva](https://carchedimarco88-jpg.github.io/Progetto_AIFA_Pharma/dashboard.html).

---

# Risultati e discussione

---

## Query SQL

### Query #1 – Totale spesa per anno, regione e categoria ATC lv.1

La query completa è disponibile in  
[Totale spesa per anno, regione e categoria ATC lv.1](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/queries/Totale_spesa_per_anno_regione_codATCliv1.sql)

---

## Dataset pubblico su BigQuery

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

![Confronti](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Screenshot%202025-08-23%20195415.png)
[Figura.2](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20VARIAZIONE%20CATEGORIE%20FARMACEUTICHE%20ATC%20PRE%20E%20POST%20COVID19.pdf) Confronto della spesa farmaceutica in Italia tra fase pre e la fase post Covid19 suddivisa per categoria ATC.

Questa sezione del progetto analizza la variazione di spesa farmaceutica per categoria ATC (livello 1) tra il periodo **Pre-COVID (2016–2019)** e **Post-COVID (2020–2023)**, a partire dal database ottenuto dalle tabelle open dell'AIFA.

---

## Report RMarkdown

Il file [Analisi spesa farmaceutica – RMarkdown](https://rpubs.com/CarchediFRM/1338164) contiene:

- Pulizia e aggregazione del dataset AIFA (2016–2023)
- Analisi dei trend per classe ATC
- Modellazione predittiva con Random Forest
- Visualizzazioni e confronto tra valori reali e stimati
- Discussione, limiti e proposte future

Può essere compilato in HTML o PDF direttamente da RStudio.

---

### [Dashboard Interattiva](https://carchedimarco88-jpg.github.io/Progetto_AIFA_Pharma/dashboard.html)
La dashboard analizza il consumo di farmaci in Italia dal 2016 al 2023, con visualizzazioni dinamiche e confronti regionali e terapeutici. Utilizza dati ATC per evidenziare trend, variazioni post-COVID e previsioni future.

- Visualizza una tabella interattiva con dati per anno, regione, classe ATC e spesa totale
- Mostra la distribuzione della spesa per categoria ATC tramite boxplot
- Analizza la spesa media per classe terapeutica con grafico a barre ruotate
- Confronta la spesa Pre vs Post COVID per ogni categoria ATC
- Evidenzia la spesa totale per regione, ordinata per valore
- Include una previsione automatica della spesa farmaceutica con il modello **Prophet**

### Verifica di coerenza (o validazione empirica)

Per confermare la coerenza dei dati elaborati, è stato effettuato un confronto diretto con i valori lordi pubblicati da AIFA nei report ufficiali OsMed. I dati estratti tramite script Python dai PDF istituzionali sono stati incrociati con quelli aggregati su BigQuery e normalizzati pro capite. Il confronto ha evidenziato una corrispondenza significativa tra i valori di spesa per classe ATC e regione, sia in termini di andamento temporale che di distribuzione territoriale. Questa sovrapposizione conferma la validità del processo di parsing, aggregazione e analisi, e rafforza l’affidabilità del modello predittivo come strumento di supporto alle decisioni cliniche e di politica sanitaria.

---

## Conclusioni

L’analisi dei consumi AIFA in Italia (2016–2023) ha messo in luce cambiamenti significativi in specifiche classi ATC, con implicazioni per la programmazione sanitaria e l’ottimizzazione della spesa.

![Illustrazione](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Screenshot%202025-08-23%20210329.png)
[Figura.3](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20DELLA%20SPESA%20FARMACEUTICA%20PRO%20CAPITE%20PER%20REGIONE.pdf) Analisi della spesa procapite per regione ed ATC sulla base dei dati ISTAT.

### Consumo di antineoplastici e immunomodulatori (ATC L)

Tra il 2016 e il 2023 il consumo complessivo del gruppo L è cresciuto del 45 %, passando da circa 112 a 162 DDD/1000 abitanti·die. Gran parte di questo incremento è imputabile ai sottogruppi:

- **L01 (Antineoplastici)**: aumento del 48 % (da 75 a 111 DDD)
- **L04 (Immunosoppressori)**: aumento del 42 % (da 37 a 53 DDD)

### Farmaci del sistema respiratorio (ATC R)

Il gruppo R ha registrato un incremento del 29 % nel consumo, da 210 a 270 DDD/1000 abitanti·die, soprattutto per i broncodilatatori e corticosteroidi tramite inalatori, riflettendo sia i postumi della pandemia sia cambiamenti nelle linee guida terapeutiche per BPCO e asma severo.

### Antivirali sistemici (ATC J05)

La disponibilità di nuovi antivirali orali per COVID-19 (molnupiravir, nirmatrelvir/ritonavir) e l’uso esteso dei farmaci antiretrovirali hanno portato a un aumento del 60 % (da 19 a 30 DDD/1000 abitanti·die) tra il 2020 e il 2023, con un picco di adozione a fine 2022.

### Antimicrobici per uso sistemico (ATC J01)

Nonostante le iniziative di stewardship, il consumo è salito del 12 % (da 820 a 920 DDD/1000 abitanti·die), probabilmente per l’uso preventivo in setting ospedalieri durante le ondate pandemiche e per l’incremento delle terapie combinate nei pazienti critici.

![Screenshot 2025-08-23 204158](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/Screenshot%202025-08-24%20001510.png)
[Figura.3](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20DELLA%20SPESA%20FARMACEUTICA%20PRO%20CAPITE%20PER%20REGIONE.pdf) La Heatmap ci permette di individuare valori fuori media nella spesa relle regioni per un categoria farmaceutica. Il grafico a colonne impilate ci permette di apprezzare la variazione della spesa farmaceutica in ciascun anno ed in proporzione tra categorie ATC.

## Impatto clinico e gestionale

I trend evidenziati sottolineano la necessità di:

- Rafforzare il monitoraggio dei nuovi immunoterapici e antineoplastici, per bilanciare efficacia clinica e sostenibilità economica.
- Consolidare i percorsi di cura respiratori, integrando telemonitoraggio e percorsi di riabilitazione polmonare post-COVID.
- Potenziare i programmi di appropriatezza nell’uso degli antivirali e degli antibiotici, per limitare resistenze e sprechi.

## Limiti dello studio

L’analisi si basa su dati aggregati AIFA, privi di informazioni cliniche patient-level (età, comorbidità, setting di erogazione). La mancanza di indicatori di esito costringe a interpretare i trend come proxy di utilizzo, non di efficacia.
Un limite rilevante del progetto riguarda la natura aggregata dei dati AIFA, che non consente analisi a livello di singolo paziente né l’identificazione di pattern clinici individuali. Per superare questa barriera, una possibile evoluzione del lavoro potrebbe prevedere la collaborazione con enti clinici e IRCCS, al fine di accedere a dataset anonimizzati patient-level, contenenti informazioni su diagnosi, comorbidità e terapie personalizzate. Questo permetterebbe di integrare i modelli predittivi con variabili cliniche e demografiche, migliorando la precisione delle previsioni e aprendo la strada a scenari di medicina di precisione. Inoltre, l’adozione di protocolli di interoperabilità (es. HL7 FHIR) e l’uso di ambienti sicuri per il trattamento dei dati sanitari (come data lake ospedalieri) garantirebbero il rispetto delle normative GDPR e la validità scientifica dell’approccio.

## Prospettive future

Integrare i dati AIFA con registri clinici e SDO per valutare:

- Outcome terapeutici associati alle classi L e R.
- Impatto economico-organizzativo dei nuovi antivirali.

Sviluppare un cruscotto in tempo reale basato su streaming BigQuery e dashboard interattive per fornire supporto decisionale continuo a policy maker e dirigenti sanitari.

---

*"L’intelligenza artificiale non sostituirà i medici, ma i medici che la usano sostituiranno quelli che non lo fanno." — Eric Topol*

---

## Riferimenti scientifici

- [AIFA Open Data](https://www.aifa.gov.it/open-data)

- [Monitoraggio Spesa Farmaceutica](https://www.aifa.gov.it/documents/20142/241044/Monitoraggio_Spesa_gennaio-dicembre2016_agg.pdf)

- [Open Data Popolazione Residente](https://demo.istat.it/app/?i=POS) ISTAT

- [Guida CT AI/ML AIFA](https://www.aifa.gov.it/documents/20142/871583/Guida_CT_AI_ML_v_1.0_del_24.05.2021_IT.pdf)

- [Rapporto OsMed 2023 – L’uso dei farmaci in Italia](https://www.aifa.gov.it/documents/20142/2594020/AIFA_Rapporto%20OsMed_2023.pdf)

- [Full Pharma Insights di IQVIA](https://www.iqvia.com/locations/italy/solutions/servizi-informativi/full-pharma-insights)

- [Analisi degli studi clinici: come i big data predicono il successo dei farmaci](https://editverse.com/it/Analisi-degli-studi-clinici%3A-come-i-big-data-predicono-il-successo-dei-farmaci-con-un%27accuratezza-dell%2785%25/)

- [Intelligenza artificiale nelle sperimentazioni cliniche: è l’ora della regolamentazione](https://www.agendadigitale.eu/sanita/intelligenza-artificiale-nelle-sperimentazioni-cliniche-e-lora-della-regolamentazione/)

- Appropriatezza prescrittiva come modello clinico - *UOC Formazione e Sviluppo Professionale, Regione Lazio*  
  [https://www.ausl.latina.it/attachments/article/6129/14.9.2022%20IMPAGINATO%20APPROPRIATEZZA%20PRESCRITTIVA.pdf](https://www.ausl.latina.it/attachments/article/6129/14.9.2022%20IMPAGINATO%20APPROPRIATEZZA%20PRESCRITTIVA.pdf)

- Rapporto sull’uso dei farmaci durante l’epidemia COVID‐19 - *AIFA – Osservatorio Nazionale sull’impiego dei Medicinali*  
  [https://www.aifa.gov.it/documents/20142/1202341/AIFA_Rapporto_uso_farmaci_durante_epidemia_COVID-19.pdf](https://www.aifa.gov.it/documents/20142/1202341/AIFA_Rapporto_uso_farmaci_durante_epidemia_COVID-19.pdf)

- Medicina di precisione e sostenibilità: strumenti giuridici tra LEA e Regioni -  *Fausto Massimino*  
[https://www.academia.edu/45059915/Medicina_di_precisione_e_sostenibilit%C3%A0_strumenti_giuridici_tra_LEA_e_Regioni](https://www.academia.edu/45059915/Medicina_di_precisione_e_sostenibilit%C3%A0_strumenti_giuridici_tra_LEA_e_Regioni)


