# Faça um program que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2

altura = float(input('Digite a altura da parede (m): '))
largura = float(input('Digite a largura da parede (m): '))

area = altura * largura

litro = area / 2

print(f'Sua parede tem a dimensão de {altura} x {largura} e sua área é de {area}m²')
print(f'Para pintar a parede irá precisar de {litro:.2f}L de tinta.')
