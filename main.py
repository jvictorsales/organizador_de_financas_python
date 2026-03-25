from typing import List

from banco_de_transacoes import BancoDeTransacoes
from transacao import Transacao

def exibir_transacoes(minhas_transacoes: List['Transacao']) -> None:
    for transacao in minhas_transacoes:
        print(transacao)

if __name__ == '__main__':
    CAMINHO_ARQUIVO = 'transacoes.json'

    transacao_1 = Transacao('ganho', 3000, 'salario', '2026-03-05')
    transacao_2 = Transacao('gasto', 1000, 'feira', '2026-03-05')
    transacao_3 = Transacao('ganho', 500, 'freelancer', '2026-03-05')
    transacao_4 = Transacao('gasto', 1500, 'cartão', '2026-03-05')

    bd_transacoes = BancoDeTransacoes(CAMINHO_ARQUIVO)
    minhas_transacoes = bd_transacoes.carregar_dados()
    # minhas_transacoes.append(transacao_1)
    # minhas_transacoes.append(transacao_2)
    # minhas_transacoes.append(transacao_3)
    # minhas_transacoes.append(transacao_4)

    minhas_transacoes.extend([
        transacao_1,
        transacao_2,
        transacao_3,
        transacao_4
    ])

    bd_transacoes.salvar_dados(minhas_transacoes)

    exibir_transacoes(minhas_transacoes)
