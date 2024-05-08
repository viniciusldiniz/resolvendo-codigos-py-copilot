
# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
def concatenar_dados(info1, info2):
    """
    Aqui vamos estar concatenando 
    dois dados diferentes em uma única 
    string.
    
    Args:
    - Info1: O primeiro dado a ser concatenado.
    - Info2: O segundo dado a ser concatenado.
    
    resultado:
    - A string resultante da concatenação dos dois dados.
    """
# Recebendo os dados do usuário
info1 = input("Digite o primeiro dado: ")  
info2 = input("Digite o segundo dado: ")

# Chamando a função para concatenar os dados
resultado = info1+ " "+ info2

# Exibindo o resultado
print("Os dados concatenados são: ", resultado)
