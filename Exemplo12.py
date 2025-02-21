# Use a palavra-chave global se quiser alterar
# uma variável global dentro de uma função.

def minhaFuncao():
    global x
    x = "Multiplataforma"

minhaFuncao()

print("Desenvolvimento " + x)
