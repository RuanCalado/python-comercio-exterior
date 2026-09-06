# Exercicio de loop

produtos = ["Pneu 14.00-24", "Pneu 17.5-25", "Pneu 14.5-25", "Pneu 12.00-24", "Pneu 10.00-20"]

for produto in produtos:
    print(produto)

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

for item in itens:
    print("Código:", item["codigo"])
    print("Produto:", item["produto"])
    print("Quantidade Invoice:", item["quantidade_invoice"])
    print("Quantidade Pl:", item["quantidade_pl"])

    if item ["quantidade_invoice"] == item ["quantidade_pl"]:
        print("OK: quantidades conferem.")
    else:
        diferenca = abs(item["quantidade_invoice"] - item["quantidade_pl"])
        print("ALERTA: quantidades divergem.")
        print("Diferença:", diferenca)
        if item ["quantidade_invoice"] > item ["quantidade_pl"]:
            print("A Invoice possui", diferenca, "itens a mais que o PL.")
        else:
            print("O PL possui", diferenca, "itens  a mais que a Invoice.")

    print("--------------------------------")