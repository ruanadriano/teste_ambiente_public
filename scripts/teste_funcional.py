import sys
import random

# Simula execução de cálculo de erro
erro_atual = 6
erro_anterior = 7

print(f"Erro atual simulado: {erro_atual}%")
print(f"Erro anterior simulado: {erro_anterior}%")

if erro_atual >= 5.0 and erro_anterior >= 5.0:
    print("Dois erros consecutivos >= 5%. Falhando.")
    sys.exit(1)
else:
    print("Teste funcional simulado passou.")
    sys.exit(0)
