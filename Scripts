#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfplumber
import pandas as pd
import re
import os

# Percorsi
PDF_PATH   = "../data/ANALISI VARIAZIONE CATEGORIE FARMACEUTICHE ATC PRE E POST COVID19.pdf"
OUTPUT_DIR = "../outputs"
CSV_NAME   = "atc_variation.csv"

def parse_currency(val: str) -> float:
    """Converti '2.508.502.565,80 €' → 2508502565.80"""
    num = val.replace(" ", "")            # rimuove spazi
    num = num.replace(".", "").replace(",", ".")  
    num = re.sub(r"[^\d\.]", "", num)     # tiene solo cifre e punto
    return float(num) if num else 0.0

def extract_table_from_pdf(path: str) -> pd.DataFrame:
    """Estrae la prima tabella dalla prima pagina del PDF."""
    with pdfplumber.open(path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    return df

def compute_variation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggiunge la colonna 'Δ€' (Post – Pre) e
    mantiene solo le colonne utili.
    """
    pre_col  = "Spesa Pre COVID19 2016-2019"
    post_col = "Spesa Post COVID19 2020-2023"

    df[pre_col]  = df[pre_col].apply(parse_currency)
    df[post_col] = df[post_col].apply(parse_currency)
    df["Δ€"]     = df[post_col] - df[pre_col]

    return df[["Categoria ATC Livello 1", pre_col, post_col, "Δ€"]]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df_raw = extract_table_from_pdf(PDF_PATH)
    df_var = compute_variation(df_raw)

    output_path = os.path.join(OUTPUT_DIR, CSV_NAME)
    df_var.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Dati salvati in {output_path}")

if __name__ == "__main__":
    main()
