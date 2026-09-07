def calcular_diferenca(quantidade_invoice, quantidade_pl):
    return abs(quantidade_invoice - quantidade_pl)

def validar_quantidade(quantidade_invoice, quantidade_pl):
    if quantidade_invoice == quantidade_invoice:
        return "OK"
    else: "DIVERGÊNCIA"

def formatar_numero(valor):
    numero_formatado = f"{valor:,.2f}"
    numero_formatado = numero_formatado.replace(",", "X")
    numero_formatado = numero_formatado.replace(".", ",")
    numero_formatado = numero_formatado.replace("X", ".")
    return numero_formatado

