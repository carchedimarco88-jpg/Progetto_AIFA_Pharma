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

### 2. [Tecnologie e Metodi](#tecnologie-e-metodi)
   - [Sintesi metodologica](#sintesi-metodologica)
   - [Fasi del lavoro](#fasi-del-lavoro)

### 3. [Risultati e discussione](#risultati-e-discussione)
   - [Query SQL](#query-sql)
   - [Dataset pubblico su BigQuery](#dataset-pubblico-su-bigquery)
   - [Report statici](#report-statici)
   - [Report RMarkdown](#report-rmarkdown)
   - [Dashboard interattiva](#dashboard-interattiva)
   - [Validazione empirica](#validazione-empirica)

### • [Conclusioni](#conclusioni)

### • [Riferimenti](#riferimenti)


---

## Abstract
*L’epidemiologia e la statistica rappresentano strumenti fondamentali per comprendere la distribuzione e l’andamento delle malattie, identificare fattori di rischio e valutare l’efficacia degli interventi sanitari. L’integrazione di metodi statistici avanzati con dati epidemiologici consente di trasformare informazioni grezze in evidenze utili per il decision‑making in sanità pubblica. In questo progetto, ho applicato tecniche di analisi statistica e modelli predittivi (ARIMA, Prophet, Random Forest) all’analisi della spesa farmaceutica italiana, utilizzando dati provenienti da BigQuery. L’obiettivo è stato individuare trend temporali, differenze regionali e principali driver di spesa, fornendo scenari previsionali con errore medio inferiore al 5%. I risultati evidenziano come l’uso combinato di epidemiologia e data science possa supportare una gestione più efficiente delle risorse e contribuire a politiche sanitarie basate su evidenze.*

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

![GRAFICO1](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Screenshot%202025-08-23%20195157.png)
[Figura.1](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20VARIAZIONE%20CATEGORIE%20FARMACEUTICHE%20ATC%20PRE%20E%20POST%20COVID19.pdf) Classifica delle categorie farmaceutiche ATC in Italia in funzione della variazione di spesa nei periodi pre e post Covid-19.

### Domanda di ricerca
Quali classi di farmaci mostrano un aumento significativo nel consumo tra il 2016 e il 2023 e come possiamo prevedere il consumo futuro per supportare decisioni di politica sanitaria e medicina di precisione.

La domanda è:
- Quantitativa (analisi e modelli)
- Applicabile (politiche sanitarie)
- Innovativa (medicina personalizzata)

---

# Tecnologie e Metodi
 
| Strumento    | Utilizzo principale                                     |
|--------------|----------------------------------------------------------|
| BigQuery     | hosting e interrogazione del dataset AIFA                |
| SQL          | estrazione, aggregazione e preparazione dei dati         |
| Python       | pulizia automatizzata, estrazione dati da PDF            |
| Excel        | analisi preliminare, incrocio con dati ISTAT             |
| R            | modellazione predittiva e report automatici con RMarkdown |

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

## Risultati chiave

- Individuazione delle classi ATC con variazioni di consumo più marcate  
- Previsioni di consumo per il triennio successivo  
- Dashboard e report per stakeholder non tecnici  
- Dataset AIFA 2016–2023 pubblicato su BigQuery  

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

![GRAFICO2](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Screenshot%202025-08-23%20195415.png)
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

### Dashboard Interattiva
La dashboard analizza il consumo di farmaci in Italia dal 2016 al 2023, con visualizzazioni dinamiche e confronti regionali e terapeutici. Utilizza dati ATC per evidenziare trend, variazioni post-COVID e previsioni future [Dashboard Interattiva](https://carchedimarco88-jpg.github.io/Progetto_AIFA_Pharma/dashboard.html).

- Visualizza una tabella interattiva con dati per anno, regione, classe ATC e spesa totale
- Mostra la distribuzione della spesa per categoria ATC tramite boxplot
- Analizza la spesa media per classe terapeutica con grafico a barre ruotate
- Confronta la spesa Pre vs Post COVID per ogni categoria ATC
- Evidenzia la spesa totale per regione, ordinata per valore
- Include una previsione automatica della spesa farmaceutica con il modello **Prophet**

### Validazione empirica

Per confermare la coerenza dei dati elaborati, è stato effettuato un confronto diretto con i valori lordi pubblicati da AIFA nei report ufficiali OsMed. I dati estratti tramite script Python dai PDF istituzionali sono stati incrociati con quelli aggregati su BigQuery e normalizzati pro capite. Il confronto ha evidenziato una corrispondenza significativa tra i valori di spesa per classe ATC e regione, sia in termini di andamento temporale che di distribuzione territoriale. Questa sovrapposizione conferma la validità del processo di parsing, aggregazione e analisi, e rafforza l’affidabilità del modello predittivo come strumento di supporto alle decisioni cliniche e di politica sanitaria.

---

## Conclusioni

L’analisi dei consumi AIFA in Italia (2016–2023) ha messo in luce cambiamenti significativi in specifiche classi ATC, con implicazioni per la programmazione sanitaria e l’ottimizzazione della spesa.

![GRAFICO3](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/GRAFICO3.png)
[Figura.3](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/ANALISI%20DELLA%20SPESA%20FARMACEUTICA%20PRO%20CAPITE%20PER%20REGIONE.pdf) Analisi della spesa procapite per regione ed ATC sulla base dei dati ISTAT.

L’andamento della spesa farmaceutica in Italia tra 2016 e 2023 evidenzia un picco eccezionale nel 2020, seguito da un rientro graduale, ma con una ricomposizione strutturale del mix terapeutico e forti differenze territoriali. La spesa pro capite nazionale passa da €137,20 nel 2019 a €161,53 nel 2020, per poi scendere a €138,37 nel 2022 e €132,60 nel 2023. Nel confronto tra periodi pre‑COVID (2016–2019) e post‑COVID (2020–2023), il totale passa da €34,47 mld a €34,97 mld (+50 mln; +1,45%), con massimo storico nel 2020 a €9,63 mld e minimo relativo nel 2023 a €7,82 mld. Questi elementi indicano che l’emergenza ha spinto temporaneamente la spesa verso l’alto, mentre la normalizzazione successiva non ha ripristinato il “vecchio” mix: il budget oggi si distribuisce in modo diverso tra le classi ATC.

---

## Ricomposizione del mix terapeutico

Il confronto pre/post pandemia mette in luce spostamenti non transitori. Crescono in valore assoluto le categorie C - Cardiovascolare (+€521,2 mln; +20,78%), V - Vari (+€468,2 mln; +24,45%), P - Antiparassitari (+€459,6 mln; +25,76%), A - Gastrointestinale (+€283,8 mln; +13,18%) e B - Sangue (+€178,7 mln; +6,87%). Calano S - Organi di senso (−€717,5 mln; −26,47%), D - Dermatologici (−€440,0 mln; −15,53%), J - Antimicrobici sistemici (−€283,2 mln; −10,36%), N Sistema nervoso (−€212,7 mln; −10,73%) e, marginalmente, M Muscolo‑scheletrico (−€56,8 mln; −2,36%). Il ranking si riallinea: C - guadagna il 1° posto (dal 9°), S - scende dal 4° al 13°, D - dal 2° al 9°, J - dal 3° al 7°. La dispersione tra categorie aumenta leggermente nel post, segnale di maggiore variabilità interna.

Questa ricomposizione suggerisce tre priorità:  
1. La spesa privilegia la gestione cronica (C - Cardiovascolare, A - Gastrointestinale), che richiede continuità terapeutica e approvvigionamenti stabili.  
2. Le categorie Vari e Antiparassitari (V, P) riflettono pressioni su voci trasversali o legate a contingenze.
3. La contrazione di S, D ed N è coerente con la riduzione degli accessi e delle prestazioni elettive nel biennio pandemico, con un recupero ancora incompleto, per cui servono budget flessibili capaci di accompagnare il rimbalzo ambulatoriale.

---

## Picco, rientro e normalizzazione differenziale

Il 2020 amplifica le componenti sensibili all’emergenza; il 2021 avvia un riassestamento; il 2022–2023 consolidano il rientro sotto i livelli 2018–2019. La normalizzazione è differenziale: la categoria R - Sistema respiratorio, pur tra i top spender, mostra una lieve contrazione nel post (−1% medio), coerente con la riduzione dopo i picchi emergenziali; gli antineoplastici e immunomodulatori mantiengono un peso elevato e stabile, coerente con la continuità dei percorsi specialistici. Il quadro complessivo è una riallocazione della spesa verso categorie ad alta cronicità e ad alto impatto specialistico, con persistente debolezza delle aree elettive non ancora tornate ai volumi pre‑pandemici.

---

## Eterogeneità territoriale e rischio di disequità

Nel quinquennio 2019–2023, la media nazionale pro capite è €145,50, ma le distanze sono estreme: Valle d’Aosta (€2.988) e Molise (€918) sono multipli della media; Trentino‑Alto Adige (€630) resta stabilmente elevato. All’opposto, Lombardia (€47,97), Campania (€67,19) e Lazio (€65,03) presentano valori persistentemente inferiori. Il rapporto VdA/Lombardia sfiora 62×, riflesso dell’effetto dimensionale e del peso di spese fisse su bacini demografici ridotti. La volatilità di Basilicata (da €387 a €914), Sardegna (da €338 a €156 nel 2020 con successiva risalita) e Molise (picco €1.135 nel 2021) indica che strategie di acquisto e gestione stock devono essere calibrate sul rischio di shock locali e sulla dimensione demografica: in regioni piccole, l’attivazione di poche terapie ad altissimo costo o la centralizzazione di percorsi specialistici può ribaltare i valori pro capite di un intero anno.

Una pianificazione efficace richiede cluster regionali per dimensione e profilo clinico, con confronto sistematico di scostamenti di spesa pro capite, costo medio per trattamento e mix ATC rispetto a benchmark nazionali, supportati da dashboard interattive e monitoraggio continuo.

---

## Implicazioni operative per acquisti e governo della spesa

L’obiettivo non è ridurre indiscriminatamente la spesa, ma allineare procurement, contratti e budget ai profili di crescita e alla variabilità territoriale.

- **Classi in crescita strutturale**: contratti pluriennali con opzioni di volume; aggregazione d’acquisto multi‑azienda; previsioni rolling trimestrali per prevenire rotture di stock; preferenziazioni terapeutiche e switch assistiti dove esistono alternative equivalenti; per L, accordi basati su esiti e risk‑sharing, rapida adozione di biosimilari e managed entry agreements, governance dei centri prescrittori per ridurre variabilità intra‑regionale.
- **Aree in calo o in recupero**: budget flessibili e indicatori sentinella sui volumi ambulatoriali; gare con lotti dinamici per riallineare le quantità senza oversupply; pianificazione del recupero liste di attesa specialistiche; per J, rafforzamento della stewardship con criteri di acquisto aderenti a linee guida e auditing prescrittivo abbinato a dashboard di uso/spesa.
- **Procurement e mitigazione del rischio**: pooling interregionale per regioni piccole/ad alta volatilità; benchmarking prezzi centralizzato; clausole di indicizzazione per shock di filiera; dual sourcing per categorie critiche; pianificazione rolling a 12 mesi con scenari alto‑medio‑basso e soglie di riordino dinamiche basate su lead time e variabilità storica.
- **Misurazione e accountability**: KPI di cruscotto su costo medio per paziente nelle top classi di spesa, tasso di adozione di biosimilari, scostamento mensile dal forecast per classe e area vasta, incidenza delle classi L‑C‑A sulla spesa e loro varianza intra‑regionale, tassi di appropriatezza per antimicrobici rispetto a linee guida; revisione trimestrale congiunta acquisti‑farmacia ospedaliera‑clinici per riallineare volumi e mix.

---

## Sintesi finale

Il sistema è uscito dalla fase emergenziale con spesa totale normalizzata ma con un mix più cronico‑specialistico. Le priorità di governo sono: garantire continuità di approvvigionamento nelle classi in crescita, adottare contratti basati su valore per terapie ad alto impatto, rafforzare stewardship e appropriatezza nelle aree a rischio di uso non ottimale, e ridurre la volatilità territoriale. La combinazione di procurement intelligente, misurazione trasparente e confronto interregionale continuo rappresenta la via più concreta per migliorare efficienza ed equità nella spesa farmaceutica.



![GRAFICO4](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/raw/main/Grafico4.png)
[Figura.3](https://github.com/carchedimarco88-jpg/Progetto_AIFA_Pharma/blob/main/2%20-%20ANALISI%20DELLA%20SPESA%20FARMACEUTICA%20PRO%20CAPITE%20PER%20REGIONE.pdf) La Heatmap ci permette di individuare valori fuori media nella spesa relle regioni per un categoria farmaceutica. Il grafico a colonne impilate evidenzia la variazione della spesa farmaceutica in ciascun anno ed in proporzione tra categorie ATC.

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


