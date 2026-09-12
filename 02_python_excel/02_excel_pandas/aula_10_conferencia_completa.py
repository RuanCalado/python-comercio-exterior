import pandas as pd

invoice = pd.read_excel(
    "02_python_excel/02_excel_pandas/invoice_aula10.xlsx",
   dtype={
       "codigo": str,
        "ncm": str
       }
)

packing_list = pd.read_excel(
    "02_python_excel/02_excel_pandas/packing_list_aula10.xlsx",
    dtype={
        "codigo": str,
        "ncm": str
        }
)

invoice["codigo"] = invoice["codigo"].str.zfill(3)
packing_list["codigo"] = packing_list["codigo"].str.zfill(3)

print("INVOICE")
print(invoice)

print()

print("PACKING LIST")
print(packing_list)

conferencia =pd.merge(
    invoice,
    packing_list,
    on="codigo",
    how="inner"
)

conferencia["valor_total"] = (
    conferencia["quantidade_invoice"]
    * conferencia["valor_unitario"]
)

print()
print("CONFERÊNCIA")
print(conferencia)

conferencia["diferenca"] = (
    conferencia["quantidade_invoice"]
    - conferencia["quantidade_pl"]
).abs()

conferencia["status"]  ="OK"

conferencia.loc[
    conferencia["quantidade_invoice"] != conferencia["quantidade_pl"],
    "status"
    ] = "DIVERGÊNCIA"

conferencia["status_peso"] = "OK"

conferencia.loc[
    conferencia["peso_bruto"] < conferencia["peso_liquido"],
    "status_peso"
] = "ERRO DE PESO"

conferencia["peso_liquido_unitario"] = (
    conferencia["peso_liquido"]
    / conferencia["quantidade_pl"]
)

conferencia["peso_bruto_unitario"] = (
    conferencia["peso_bruto"]
    / conferencia["quantidade_pl"]
)

conferencia["status_geral"] = "OK"

conferencia.loc[
    (conferencia["status"] == "DIVERGÊNCIA")
    & (conferencia["status_peso"] == "OK"),
    "status_geral"
] = "DIVERGÊNCIA"

conferencia.loc[
    (conferencia["status"] == "OK")
    & (conferencia["status_peso"] == "ERRO DE PESO"),
    "status_geral"
] = "ERRO DE PESO"

conferencia.loc[
    (conferencia["status"] == "DIVERGÊNCIA")
    & (conferencia["status_peso"] == "ERRO DE PESO"),
    "status_geral"
] = "REVISAR"

print()
print("CONFERÊNCIA FINAL")
print(conferencia)

caminho_saida = (
    "02_python_excel/02_excel_pandas/"
    "resultado_conferencia_aula10.xlsx"
)

conferencia.to_excel(
    caminho_saida,
    index=False
)

print("Arquivo da Aula 10 criado com sucesso.")
print("Arquivo da Aula 10 criado com sucesso.")