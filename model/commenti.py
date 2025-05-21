class Commenti:

    def __init__(self, id=None, data_ora=None, contenuto=None, id_post=None, id_utente=None, nickname=None):
        self.id = id
        self.data_ora = data_ora
        self.contenuto = contenuto
        self.id_post = id_post
        self.id_utente = id_utente
        self.nickname = nickname


    # metodo di deserializzazione
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione
    def serializzazione(self):
        return self.__dict__


    # metodo di serializzazione
    def serializzazione_per_post(self):
        return {
            "id": self.id,
            "data_ora": self.data_ora,
            "contenuto": self.contenuto,
            "nickname": self.nickname,
        }