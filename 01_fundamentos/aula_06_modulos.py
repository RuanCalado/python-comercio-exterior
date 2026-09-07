# Aula 06 — Módulos, imports e organização do código

from utilitarios import calcular_diferenca, validar_quantidade, formatar_numero

quantidade_inovice = 100
quantidade_pl = 95

status = validar_quantidade(
    quantidade_inovice,
    quantidade_pl
)

diferenca = calcular_diferenca(
    quantidade_inovice,
    quantidade_pl
)

peso_total = 16325.0

print("Status:", status)
print("Diferença:", diferenca)
print("Peso total:", formatar_numero(peso_total), "kg")