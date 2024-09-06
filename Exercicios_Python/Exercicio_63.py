# Sequência de Fibonacci
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0  # O termo 1 vai iniciar com o número 0
t2 = 1  # O termo 2 vai iniciar com o número 1
print(f'{t1} -> {t2}', end=' ') 
cont = 3  # O contador vai começar do número 3 porque já tiveram 2 contagens (t1, t2)

# Loop: se o contador for menor ou igual ao número do termo que o usuário digitou, o loop é executado.
while cont <= termos:
    t3 = t1 + t2  # O termo 3 vai receber a soma do t1 e t2
    print(f'-> {t3}', end=' ')
    t1 = t2  # Inicio da soma, de 1 em 1. O t1 passa a ser t2.
    t2 = t3  # E o t2 passa a ser o t3
    cont += 1  # Contador de 1 em 1

print('-> FIM')