# Projeto: Organizador de Finanças

import os
import json
from datetime import datetime

def carregar_transacoes():

    if os.path.exists('transacoes.json'):
        with open('transacoes.json') as arquivo:
            transacoes = json.load(arquivo)
            return transacoes      
    else:
        return []

def salvar_transacoes(transacoes):
    with open('transacoes.json', 'w') as arquivo:
        json.dump(transacoes, arquivo, indent=4, ensure_ascii=False)


def registrar_transacao(tipo, transacoes):

    valor = input('Digite o valor: ')

    try:
        valor_float = float(valor)
    except ValueError:
        print('Valor inserido foi inválido, tente novamente.')
        return
    
    descricao = input('Digite a descrição: ')

    data_atual = datetime.today().strftime('%Y-%m-%d')

    transacao = {
        'tipo': tipo,
        'valor': valor_float,
        'descricao': descricao,
        'data': data_atual
    }

    transacoes.append(transacao)


def calcular_saldo(transacoes):
    
    saldo = 0

    for transacao in transacoes:
        
        if transacao['tipo'] == 'ganho':
            saldo += transacao['valor']

        elif transacao['tipo'] == 'gasto':
            saldo -= transacao['valor']

    return saldo

def exibir_saldo(transacoes):

    saldo = calcular_saldo(transacoes)

    print()
    print('===== SALDO ATUAL =====')
    print(f'Saldo atual: R$ {saldo:.2f}')
    print()


def listar_transacoes(transacoes):
    if not transacoes:
        print('Nenhuma transação cadastrada.')
        return

    print('===== TRANSAÇÕES =====')
    print()
    
    for transacao in transacoes:
        print(f"{transacao['tipo']:6} | {transacao['valor']:8} | {transacao['descricao']:15} | {transacao['data']}")

def mostrar_menu():
    print()
    print('===== ORGANIZADOR DE FINANÇAS =====')
    print()
    print('1 - Registrar ganho')
    print('2 - Registrar gasto')
    print('3 - Listar transações')
    print('4 - Ver saldo')
    print('0 - Sair')
    print()

transacoes = carregar_transacoes()

while True:

    mostrar_menu()

    opcao_usuario = input('Escolha uma opção: ')
    print()

    if opcao_usuario.isdigit():
        opcao_usuario = int(opcao_usuario)
    else:
        print('Opção inserida é inválida, tente novamente.')
        continue

    if opcao_usuario == 1:
        registrar_transacao('ganho', transacoes)
        salvar_transacoes(transacoes)
    elif opcao_usuario == 2:
        registrar_transacao('gasto', transacoes)
        salvar_transacoes(transacoes)
    elif opcao_usuario == 3:
        listar_transacoes(transacoes)
    elif opcao_usuario == 4:
        exibir_saldo(transacoes)
    elif opcao_usuario == 0:
        print('Saindo...')
        break
    else:
        print('Opção inexistente, tente novamente.')
