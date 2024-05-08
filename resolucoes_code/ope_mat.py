# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ")
if operador == '+':
    print(numero1 + numero2)
elif operador == '-':
    print(numero1 - numero2)
elif operador == '*':
    print(numero1 * numero2)2
elif operador == '/':
    print(numero1 / numero2)
else:
    print("Operador inválido.")

