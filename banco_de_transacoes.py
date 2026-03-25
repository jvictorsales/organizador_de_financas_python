import json
from typing import List

from transacao import Transacao

class BancoDeTransacoes:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def carregar_dados(self) -> List['Transacao']:
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo)
                return [Transacao.from_dict(dado) for dado in dados]
        except FileNotFoundError:
            return []
    
    def salvar_dados(self, dados: List['Transacao']) -> None:
        dados_dict = [dado.to_dict() for dado in dados]
        with open(self.caminho_arquivo, 'w', encoding='utf8') as arquivo:
            json.dump(dados_dict, arquivo, indent=2, ensure_ascii=False)

