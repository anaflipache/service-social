class LikeApposti:

    def __init__(self, id=None, id_post=None, id_utente=None):
        self.id = id
        self.id_post = id_post
        self.id_utente = id_utente


    # metodo di deserializzazione
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione
    def serializzazione(self):
        return self.__dict__
