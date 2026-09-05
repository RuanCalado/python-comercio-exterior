# Exercício: validação simples

quantidade_invoice = 120
quantidade_pl = 100

diferenca = abs(quantidade_invoice - quantidade_pl)

if quantidade_invoice > quantidade_pl:
    print("A Invoice possui", diferenca, "itens a mais que o PL")
elif quantidade_invoice < quantidade_pl:
    print("A Invoice possui", diferenca, "itens a menos que o PL")
else:
    print("OK: as quantidades conferem.")

print("Quantidade Invoice:", quantidade_invoice)
print("Quantidade Pl:", quantidade_pl)
print("Diferença:", diferenca)