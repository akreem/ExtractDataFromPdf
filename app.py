import pdfplumber
import pandas as pd
import json

fichier_pdf = "fichier.pdf"

# Lecture du PDF avec pdfplumber
with pdfplumber.open(fichier_pdf) as pdf:
    all_tables = []
    for page in pdf.pages:
        extracted_tables = page.extract_tables()
        for table in extracted_tables:
            table_data = []
            for row in table:
                table_data.append(row)
            all_tables.append(table_data)

json_data = json.dumps(all_tables, ensure_ascii=False)
data = json.loads(json_data)

index_to_cut = data[0].index([
    "",
    "Numéro produit référence",
    None,
    "Nom produit variante",
    None,
    "Composition",
    None,
    "N° Lot",
    "No de série",
    "Nomenclature\ndouanière",
    "Pays d'origine",
    "Qté (ml)",
    "PA HT (€)",
    "Valeur €",
    "Poids net (Kg)",
    ""
])
content_after_object = data[0][index_to_cut + 1:]
cleaned_data = [[item for item in row if item is not None and item != ''] for row in content_after_object]
for row in cleaned_data:
    print(row)
