from transacao import Transacao

def exibir_transacao(minhas_transacoes: list['Transacao']) -> None:
    for transacao in minhas_transacoes:
        print(f'{transacao.tipo:6} | {transacao.valor:8} | {transacao.descricao:15} | {transacao.data}')


if __name__ == '__main__':
    minhas_transacoes = Transacao.carregar_transacoes()

    transacao_1 = Transacao('ganho', 4000, 'salario', '2026-03-10')
    transacao_2 = Transacao('gasto', 1000, 'feira', '2026-03-10')

    minhas_transacoes.append(transacao_1)
    minhas_transacoes.append(transacao_2)

    Transacao.salvar_transacoes(minhas_transacoes)

    exibir_transacao(minhas_transacoes)
