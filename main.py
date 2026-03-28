from datetime import datetime

from banco_de_transacoes import BancoDeTransacoes
from transacao import Transacao

def menu():
    print()
    print('===== ORGANIZADOR DE FINANÇAS =====')
    print()
    print('1 - registrar ganho')
    print('2 - registrar gasto')
    print('3 - listar transações')
    print('4 - ver saldo')
    print('0 - sair')
    print()


def registrar_transacao(tipo):

    valor = input('valor: ')

    try:
        valor = float(valor)
    except ValueError:
        print()
        print('Valor inserido é inválido, tente novamente...')
        return

    descricao = input('descrição: ')
    data = datetime.today().strftime('%Y-%m-%d')

    transacao = Transacao(tipo, valor, descricao, data)
    transacoes.append(transacao)

    bd_transacoes.salvar_dados(transacoes)

def listar_transacoes(transacoes):
    for transacao in transacoes:
        print(transacao)

def ver_saldo(transacoes):
    ...


if __name__ == '__main__':
    CAMINHO_ARQUIVO = 'transacoes.json'

    bd_transacoes = BancoDeTransacoes(CAMINHO_ARQUIVO)
    transacoes = bd_transacoes.carregar_dados()
    
    comandos_menu = {
        1: lambda: registrar_transacao('ganho'),
        2: lambda: registrar_transacao('gasto'),
        3: lambda: listar_transacoes(transacoes),
        4: lambda: ver_saldo(transacoes),
    }

    while True:
        menu()
        opcao = input('Escolha uma opção: ')

        if not opcao.isdigit():
            print('Opção inválida, tente novamente...')
            continue

        opcao = int(opcao)
        
        if opcao == 0:
            print()
            print('Saindo...')
            print()
            break

        executa_comando = comandos_menu.get(opcao, lambda: print('Opção não existe, tente novamente...'))
        executa_comando()
