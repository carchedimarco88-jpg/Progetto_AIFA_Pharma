#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfplumber
import pandas as pd
import re
import os


PDF_PATH = "reports/ANALISI VARIAZIONE CATEGORIE FARMACEUTICHE ATC PRE E POST COVID19.pdf"
OUTPUT_DIR = "outputs"
CSV_NAME = "atc_variation.csv"

def parse_currency(val: str) -> float:
    num = val.replace(" ", "").replace(".", "").replace(",", ".")
    num = re.sub(r"[^\d\.]", "", num)
    return float(num) if num else 0.0

def extract_table_from_pdf(path: str) -> pd.DataFrame:
    with pdfplumber.open(path) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
    df = pd.DataFrame(table[1:], columns=table[0])
    print("📌 Colonne trovate nel PDF:")
    for col in df.columns:
        print(f"– {col}")
    return df

def compute_variation(df: pd.DataFrame) -> pd.DataFrame:
    # Trova le colonne corrette
    pre_col  = [c for c in df.columns if "Pre COVID" in c][0]
    post_col = [c for c in df.columns if "Post COVID" in c][0]
    label_col = [c for c in df.columns if "Categoria" in c][0]

    df[pre_col]  = df[pre_col].apply(parse_currency)
    df[post_col] = df[post_col].apply(parse_currency)
    df["Δ€"]     = df[post_col] - df[pre_col]

    return df[[label_col, pre_col, post_col, "Δ€"]]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df_raw = extract_table_from_pdf(PDF_PATH)
    df_var = compute_variation(df_raw)
    out_path = os.path.join(OUTPUT_DIR, CSV_NAME)
    df_var.to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"\n✅ Dati salvati in: {out_path}")

if __name__ == "__main__":
    main()
