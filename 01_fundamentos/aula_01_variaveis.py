# Primeiro exercício: variáveis e cálculo de peso

produto = input("informe o produto:")
quantidade = int(input("Digite a quantidade: "))
peso_unitario = float(input("Digite o peso unitário:"))

peso_total = quantidade * peso_unitario
if peso_total <= 1000:
    print("Carga leve")
elif peso_total <=5000:
    print("Carga média")
else:
    print("Carga pesada")

print("Produto:", produto)
print("Quantidade:", quantidade)
print("Peso unitário:", peso_unitario, "kg")
print("Peso Total:", peso_total, "kg")
