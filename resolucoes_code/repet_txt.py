# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def repetir_texto(string, numero):
# Recebendo a string e o número de repetições do usuário
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Exibindo o resultado
print("O texto repetido é:" + (string+' ') * numero)
