# Se você criar uma variável com o mesmo nome dentro de uma função essa
# variável será local e só poderá ser usada dentro da função.
# A variável global com o mesmo nome permanecerá como era, global
# e com o valor original.

# Variável Global

x = "A Aula de mineração de dados "

def minhaFuncao():
    x = "Desenvolvimento de Software"
    print("Melhor curso da FATEC" + x)

minhaFuncao()

print("Seja bem vindo " + x)
