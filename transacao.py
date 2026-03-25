import json
from typing import List

CAMINHO_ARQUIVO = 'transacoes.json'

class Transacao:

    def __init__(self, tipo, valor, descricao, data):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.data = data

    def from_obj_to_dict(self) -> dict:
        return {
            'tipo': self.tipo,
            'valor': self.valor,
            'descricao': self.descricao,
            'data': self.data,
        }
    
    @classmethod
    def from_dict_to_obj(cls, dados: dict):
        return cls(
            dados['tipo'],
            dados['valor'],
            dados['descricao'],
            dados['data']
        )

    @classmethod
    def carregar_transacoes(cls) -> List['Transacao']:
        try:
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo)
                return [cls.from_dict_to_obj(dado) for dado in dados]
        except FileNotFoundError:
            return []

    @staticmethod
    def salvar_transacoes(transacoes: List['Transacao']) -> None:
        dados = [transacao.from_obj_to_dict() for transacao in transacoes]

        with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)

