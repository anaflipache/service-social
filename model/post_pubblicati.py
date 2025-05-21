class PostPubblicati:

    def __init__(self, id=None, data_ora=None, contenuto=None, utente=None, numero_like=0, commenti=None, nickname=None):
        self.id = id
        self.data_ora = data_ora
        self.contenuto = contenuto
        self.utente = utente
        self.numero_like = numero_like
        self.commenti = commenti if commenti else []
        self.nickname = nickname


    # metodo di deserializzazione
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione
    def serializzazione(self):
        return self.__dict__


    # metodo di serializzazione
    def serializzazione_per_utenti(self):
        return {
            "id": self.id,
            "data_ora": self.data_ora,
            "contenuto": self.contenuto,
            "numero_like": self.numero_like,
        }


    # metodo di serializzazione
    def serializzazione_due(self):
        return {
            "id": self.id,
            "data_ora": self.data_ora,
            "nickname": self.nickname,
            "commenti": [commento.serializzazione_per_post() for commento in self.commenti]
        }
