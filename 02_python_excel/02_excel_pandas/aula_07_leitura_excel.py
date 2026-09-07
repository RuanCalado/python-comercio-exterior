import pandas as pd

tabela = pd.read_excel(
    "02_excel_pandas/invoice_teste.xlsx",
    dtype={"codigo": str}
)

tabela["codigo"] = tabela["codigo"].str.zfill(3)

tabela["peso_total"] = tabela["quantidade"] * tabela["peso_unitario"]

print(tabela)

tabela.to_excel(
    "02_excel_pandas/resultado_invoice.xlsx",
    index=False
)

print("Arquivo resultado_inovoice.xlsx criado com sucesso!")