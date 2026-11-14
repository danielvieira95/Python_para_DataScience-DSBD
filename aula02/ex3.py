# Exemplo numero float substituição , por .

#Armazena o valor digitado pelo usuario na variavel preco
preco = float(input('Digite o preco ').replace(',' , '.'))
print(f'Preço R$ {preco:.2f}')