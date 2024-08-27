# Analisando Triângulos 2.0
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
# Teste para verificar se forma ou não um triângulo
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    # Condição Aninhada
    if a == b == c:
        print('\033[1;35mEQUILÁTERO\033[m.')
    elif a != b != c != a:
        print('\033[1;35mESCALENO\033[m.')
    else:
        print('\033[1;35mISÓSCELES\033[m.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')