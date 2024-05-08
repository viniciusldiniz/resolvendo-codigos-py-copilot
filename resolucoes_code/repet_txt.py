
def repetir_texto(string, numero):
    """
    Repete uma string um número de vezes especificado.
    
    Args:
    - string: A string a ser repetida.
    - numero: O número inteiro de vezes
    
    print:
    - A string resultante da repetição do texto.
    """
# Recebendo a string e o número de repetições do usuário
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Exibindo o resultado
print("O texto repetido é:" + (string+' ') * numero)
