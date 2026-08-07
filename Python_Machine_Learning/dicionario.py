
# Exemplo de dicionário
# dicionario = {chave: valor}
# stacks = {"python": "django",
#           "java": "spring"}
#
# dicionario.clear() 'limpa o dicionario' 

frutas = {
    "morango": 2,
    "banana": 4,
    "uva": 6,
    "laranja": "podre" 
    }

''' Consultamos a chave e a busca nos retorna o valor '''
print(f"Eu tenho {frutas["banana"]} bananas.")

a = frutas["laranja"]
print(f"A laranja esta {a}.")

''' Alterando valor da chave '''
frutas["laranja"] = "docinha"
print(f"A laranja esta {frutas["laranja"]}.")

print(frutas.keys()) # Mostra as chaves do dicionário
print(frutas.values()) # Mostra os valores do dicionário
print(frutas.items()) # Mosta as chaves e os valores do dicionário