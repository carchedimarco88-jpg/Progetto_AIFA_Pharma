# METODOLOGIA

---

## Fonti dei dati

I valori di spesa utilizzati in questo progetto provengono da:  
- Portale Open Data di AIFA  
- Report ufficiali di monitoraggio della spesa farmaceutica (PDF)

---

## Definizioni

- Valore netto  
  Spesa effettiva al netto di pay-back, sconti convenzionali e altri contributi previsti da intese nazionali o regionali.

- Valore lordo  
  Spesa iniziale prima dell’applicazione dei meccanismi di recupero. Questo importo risulta sempre superiore al netto e non è incluso nel dataset principale.

---

## Meccanismi di recupero

- Pay-back obbligatorio  
  Rimborso versato dalle aziende al Servizio Sanitario Nazionale in caso di superamento dei tetti di spesa.

- Sconti convenzionali  
  Agevolazioni tariffarie concordate tra AIFA, Ministero della Salute e industrie farmaceutiche.

- Altri contributi e compensazioni  
  Voci specifiche stabilite da accordi regionali o intese temporanee.

---

## Calcolo del valore lordo (esempio)

Di seguito uno snippet Python che ricostruisce il valore lordo a partire dal netto, applicando percentuali ipotetiche di pay-back e sconto.

```python
# Input: spesa netta per anno, regione e ATC (livello 1)
dati_netti = {
    '2023': {'Lombardia': 120_000_000, 'Lazio': 95_000_000}
}

# Percentuali di pay-back e sconto (esempio)
percentuali = {
    'payback': 0.05,      # 5%
    'sconto': 0.07        # 7%
}

def ricostruisci_lordo(netto, payback_rate, sconto_rate):
    # netto = lordo * (1 - payback_rate) * (1 - sconto_rate)
    fattore_recupero = (1 - payback_rate) * (1 - sconto_rate)
    return netto / fattore_recupero

dati_lordi = {}
for anno, regioni in dati_netti.items():
    dati_lordi[anno] = {}
    for reg, valore_netto in regioni.items():
        dati_lordi[anno][reg] = ricostruisci_lordo(
            valore_netto,
            percentuali['payback'],
            percentuali['sconto']
        )

print(dati_lordi)
