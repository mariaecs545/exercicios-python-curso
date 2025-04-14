# Faça um algoritmo que leia preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o preço do produto (R$): '))

desconto = (produto * 5) / 100

valor = produto - desconto

print(f'O valor do produto após 5% de desconto é R${valor:.2f}.')
