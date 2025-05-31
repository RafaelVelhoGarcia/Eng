class Card(dict):
    def __init__(self, card_id: int):
        self._card_id = card_id  # Mudando para _card_id para manter consistência
        dict.__init__(self, _card = card_id)
    @property
    def id(self):
        return self._card_id
    
    @id.setter
    def id(self, value):
        self._card_id = value

    @classmethod
    def from_dict(cls, data):
        """
        Cria uma Card a partir de um dicionário ou objeto Card/PathCard.
        
        Args:
            data: Pode ser um dicionário ou objeto Card/PathCard
            
        Returns:
            Uma nova instância de Card ou a própria instância se já for um Card
        """
        # Se já for uma instância de Card, retorne ela mesma
        if isinstance(data, cls):
            return data
            
        # Se for um dicionário, extraia os dados
        if isinstance(data, dict):
            # Verifica se usa '_numero' ou '_card_id' como chave
            card_id = data.get('_card_id', data.get('_numero'))
            if card_id is None:
                raise ValueError("Dicionário não contém '_card_id' ou '_numero'")
            return cls(card_id)
            
        # Se for outro tipo de objeto que tem o atributo _card_id ou _numero
        if hasattr(data, '_card_id'):
            return cls(data._card_id)
        elif hasattr(data, '_numero'):
            return cls(data._numero)
            
        raise ValueError(f"Não é possível criar Card a partir do tipo: {type(data)}")

    def to_dict(self):
        """Converte o Card para um dicionário serializável"""
        return {
            '_card_id': self._card_id,
            '_type': 'Card'  # Adicionando tipo para identificação
        }

    def to_string(self):
        return f"Card(id={self._card_id})"