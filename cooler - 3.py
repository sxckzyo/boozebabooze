# Exercício 03
nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))
idade_minima = 14

print("\n--- VERIFICAÇÃO DE ACESSO ---")

if idade >= idade_minima:
    pritn(f"{nome}, seu acesso à oficina foi liberado.")
    print("Você ja possui a idade mínima exigida.")
else:
    anos_faltantes = idade_minima - idade
    print(f"{nome}, seu acesso ainda não foi liberado.")
    print(f"Faltam {anos _faltantes} anos(s) para atingir a idade mínima.")
