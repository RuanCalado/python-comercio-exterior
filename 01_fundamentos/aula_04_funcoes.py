# 1. FUNÇÕES

def calcular_diferenca(quantidade_invoice, quantidade_pl):
    diferenca = abs(quantidade_invoice - quantidade_pl)
    return diferenca

def validar_quantidades(quantidade_invoice, quantidade_pl):
    if quantidade_invoice == quantidade_pl:
        return "Ok"
    else:
       return "DIVERGÊNCIA"

# 2. DADOS

itens = [
    {
        "codigo": "001",
        "produto": "Pneu 14.00-24",
        "quantidade_invoice": 100,
        "quantidade_pl": 100
    },
    {
        "codigo": "002",
        "produto": "Pneu 17.5-25",
        "quantidade_invoice": 50,
        "quantidade_pl": 45
    }
]

# 3. INÍCIO DO PROGRAMA

print("Iniciando conferência de importação.")
print()

# 4. PROCESSAMENTO

for item in itens:
    status = validar_quantidades(
        item["quantidade_invoice"],
        item["quantidade_pl"]
    )

    print("Código:", item["codigo"])
    print("Produto:", item["produto"])
    print("Quantidade Invoice:", item["quantidade_invoice"])
    print("Quantidade PL:", item["quantidade_pl"])
    print("Status:", status)

    if status == "DIVERGÊNCIA":
        diferenca = calcular_diferenca(
            item["quantidade_invoice"],
            item["quantidade_pl"]
        )
        print("Diferença:", diferenca)

    print("--------------------------------")
