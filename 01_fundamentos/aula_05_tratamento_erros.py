# Tratamento de erros - Validação mais robusta

def formatar_numero(valor):
    numero_formatado = f"{valor:,.2f}"
    numero_formatado = numero_formatado.replace(",", "X")
    numero_formatado = numero_formatado.replace(".", ",")
    numero_formatado = numero_formatado.replace("X", ".")
    return numero_formatado

while True: 
    try:
        quantidade = int(input("Digite a quantidade:"))

        if quantidade <= 0:
            print("ERRO: a quantidade deve ser maior que zero.")
            continue

        break

    except ValueError:
        print("ERRO: informe uma quantidade numérica válida.")

while True: 
    try:
        entrada_peso = input("Digite o peso unitário: ")

        entrada_peso = entrada_peso.replace(",",".")

        peso_unitario = float(entrada_peso)

        if peso_unitario <= 0:
            print("ERRO: o peso unitário deve ser maior que zero.")
            continue

        break

    except ValueError:
        print("ERRO: informe um peso unitário válido.")

peso_total = quantidade * peso_unitario

valor_formatado = f"{peso_total:,.2f}"
valor_formatado = valor_formatado.replace(",", "X")
valor_formatado = valor_formatado.replace(".", ",")
valor_formatado = valor_formatado.replace("X", ".")

peso_total = quantidade * peso_unitario

print("--------------------------------")
print("Quantidade:", quantidade)
print("Peso unitário:", formatar_numero(peso_unitario), "kg")
print("Peso total:", formatar_numero(peso_total), "kg")
