# Gerenciador de Pagamentos
print('=-=' * 5, 'NOME DA SUA LOJA', '=-=' * 5)
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista (Dinheiro ou PIX)
[ 2 ] À vista (Cartão)
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão (C/ JUROS)''')

opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    a_vista = compras - (compras * 10 / 100)
    print(f"A sua compra de R${compras:.2f} vai custar R${a_vista:.2f}.")
elif opcao == 2:
    a_vista_cartao = compras - (compras * 5 / 100)
    print(f'A sua compra de R${compras:.2f} vai custar R${a_vista_cartao:.2f}.')
elif opcao == 3:
    valor_parcela_2x = compras / 2
    print(f'A sua compra será parcelada em 2x de R${valor_parcela_2x:.2f} SEM JUROS.'
        f'\nSua compra terá um valor de R${compras:.2f} no final.')
elif opcao == 4:
    qtd_parcelas = int(input('Quantas parcelas? '))
    juros = compras + (compras * 20 / 100)
    valor_parcelas = juros / qtd_parcelas
    print(f'Sua compra será parcelada em {qtd_parcelas}x de R${valor_parcelas:.2f} COM JUROS.'
        f'\nSua compra de R${compras:.2f} vai custar R${juros:.2f} no final.')
else:
    print('Erro! 🔴'
        '\nOpção inválida. Tente novamente!')
