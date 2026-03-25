class Transacao:
    def __init__(self, tipo, valor, descricao, data):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.data = data

    def __str__(self):
        return(f'{self.tipo:<6} | {self.valor:>8.2f} | {self.descricao:<15} | {self.data}')
    
    @classmethod
    def from_dict(cls, dados: dict) -> 'Transacao':
        return cls(
            dados['tipo'],
            dados['valor'],
            dados['descricao'],
            dados['data']
        )

    def to_dict(self) -> dict:
        return {
            'tipo': self.tipo,
            'valor': self.valor,
            'descricao': self.descricao,
            'data': self.data,
        }
