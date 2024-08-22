# Seno, Cosseno e Tangente
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem o TANGENTE de: {:.2f}'.format(angulo, tangente))