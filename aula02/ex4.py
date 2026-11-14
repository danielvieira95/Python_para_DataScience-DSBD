# Exemplo 04
'''
Exemplo 04 para receber 
vários valores 
na mesma linha utilizando split
'''

nome ,idade,cidade = input(
    "Digite o nome, idade e cidade separados por espaço: "
).split() # Armazena os valores digitados pelo usuario nas variaveis acima

idade = int(idade) # Converte a idade string para inteiro
# Conversão de valores é chamado de parse
# Exibe o nome, idade e cidade do usuario usando f-string para formatação de saida
print(f'{nome} tem {idade} anos e mora em {cidade}')