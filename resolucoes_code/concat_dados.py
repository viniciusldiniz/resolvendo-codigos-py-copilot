
# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
def concatenar_dados(info1, info2):
# Recebendo os dados do usuário
info1 = input("Digite o primeiro dado: ")  
info2 = input("Digite o segundo dado: ")

# Chamando a função para concatenar os dados
resultado = info1+ " "+ info2

# Exibindo o resultado
print("Os dados concatenados são: ", resultado)
