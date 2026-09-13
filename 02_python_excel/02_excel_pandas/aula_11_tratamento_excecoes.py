import pandas as pd

caminho_invoice = (
    "02_python_excel/02_excel_pandas/"
    "invoice_aula11.xlsx" 
)

caminho_pl = (
     "02_python_excel/02_excel_pandas/"
    "packing_list_aula11.xlsx"
)

invoice = pd.read_excel(
    caminho_invoice,
    dtype={"codigo": str}
)

packing_list = pd.read_excel(
    caminho_pl,
    dtype={"codigo":str}
)

invoice["codigo"] = invoice["codigo"].str.zfill(3)
packing_list["codigo"] = packing_list["codigo"].str.zfill(3)

print("INVOICE")
print(invoice)

print()

print("PACKING LIST")
print(packing_list)

duplicados_invoice = invoice[
    invoice["codigo"].duplicated(keep=False)
]

duplicados_pl = packing_list[
    packing_list["codigo"].duplicated(keep=False)
]

print()
print("DUPLICADO NA INVOICE")
print(duplicados_invoice)

print()
print("DUPLICADO NO PACKING LIST")
print(duplicados_pl)

if not duplicados_invoice.empty:
    raise ValueError(
        "Existem códigos duplicados na Invoice."
        "Corrija a base antes de continuar."
    )

if not duplicados_pl.empty:
    raise ValueError(
        "Existem códigos duplicados na Packing List."
        "Corrija a base antes de continuar."
    )


conferencia = pd.merge(
    invoice,
    packing_list,
    on="codigo",
    how="outer",
    indicator=True
)

conferencia["status"] = "OK"

conferencia.loc[
    conferencia["_merge"] == "left_only",
    "status"
] = "AUSENTE NO PL"

conferencia.loc[
    conferencia["_merge"] == "right_only",
    "status"
] = "AUSENTE NA INVOICE"

conferencia.loc[
    (
        conferencia["quantidade_invoice"].isna()
        | conferencia["quantidade_pl"].isna()
    )
    & (conferencia["_merge"] == "both"),
    "status"
] = "DADOS INCOMPLETOS"

conferencia.loc[
    (conferencia["_merge"] == "both")
    & (conferencia["quantidade_invoice"].notna()
    & conferencia["quantidade_pl"].notna()
    & (
        conferencia["quantidade_invoice"]
        != conferencia["quantidade_pl"]
    )
    ),
    "status"
] = "DIVERGÊNCIA"

print()
print("CONFERÊNCIA")
print(conferencia)