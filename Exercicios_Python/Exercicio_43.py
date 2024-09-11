peso = float(input('Qual é o seu peso? Kg '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)

print(f'O IMC dessa pessoa é: {imc:.1f}')
if imc < 18.5:
    print('Sua classificação é: \033[1;36mABAIXO DO PESO\033[m')
elif imc < 25:
    print('Sua classificação é: \033[1;32mNORMAL\033[m')
elif imc < 30:
    print('ATENÇÃO! 🟡 \n'
        'Sua classificação é: \033[1;33mSOBREPESO\033[m')
elif imc < 35:
    print('CUIDADO! 🔴 \n' 
        'Sua classificação é: \033[1;31mOBESIDADE GRAU I\033[m')
elif imc < 40:
    print('CUIDADO! 🔴 \n'
        'Sua classificação é: \033[1;31mOBESIDADE GRAU II\033[m')
elif imc > 40:
    print('CUIDADO! 🔴 \n'
        'Sua classificação é: \033[1;31mOBESIDADE GRAU III\033[m')