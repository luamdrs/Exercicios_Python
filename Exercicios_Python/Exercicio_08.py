medida = float(input('Quantos metros você deseja realizar a conversão? '))
km = medida * 0.001
decim = medida * 10
cm = medida * 100
mm = medida * 1000
milha = medida * 0.00062137
print(f'{medida}m equivale a {km}km.')
print(f'{medida}m equivale a {decim} decímetros.')
print(f'{medida}m equivale a {cm} centímetros.')
print(f'{medida}m equivale a {mm}mm.')
print(f'{medida}m equivale a {milha} milhas.')