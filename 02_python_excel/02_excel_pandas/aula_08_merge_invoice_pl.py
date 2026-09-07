import pandas as pd


# Leitura da Invoice
invoice = pd.read_excel(
    "02_python_excel/02_excel_pandas/invoice_aula08.xlsx",
    dtype={"codigo": str}
)


# Leitura do Packing List
packing_list = pd.read_excel(
    "02_python_excel/02_excel_pandas/packing_list_aula08.xlsx",
    dtype={"codigo": str}
)


# Padronização dos códigos
invoice["codigo"] = invoice["codigo"].str.zfill(3)
packing_list["codigo"] = packing_list["codigo"].str.zfill(3)


# Cruzamento Invoice x Packing List
conferencia = pd.merge(
    invoice,
    packing_list,
    on="codigo",
    how="outer",
    indicator=True
)


# Cálculo da diferença
conferencia["diferenca"] = (
    conferencia["quantidade_invoice"]
    - conferencia["quantidade_pl"]
).abs()


# Status inicial
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
    (conferencia["_merge"] == "both")
    & (
        conferencia["quantidade_invoice"].isna()
        | conferencia["quantidade_pl"].isna()
    ),
    "status"
] = "DADOS INCOMPLETOS"


conferencia.loc[
    (conferencia["_merge"] == "both")
    & conferencia["quantidade_invoice"].notna()
    & conferencia["quantidade_pl"].notna()
    & (
        conferencia["quantidade_invoice"]
        != conferencia["quantidade_pl"]
    ),
    "status"
] = "DIVERGÊNCIA"

print("INVOICE")
print(invoice)

print()

print("PACKING LIST")
print(packing_list)

print()

print("CONFERÊNCIA")
print(conferencia)

conferencia = conferencia.drop(columns=["_merge"])

conferencia.to_excel(
    "02_python_excel/02_excel_pandas/resultado_conferencia_aula08.xlsx",
    index=False
)

print()
print("Arquivo de conferência criado com sucesso.")
