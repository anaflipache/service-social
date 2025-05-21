class RelazioniAmicizia:

    def __init__(self, id=None, data_ora=None, stato=None, id_richiedente=None, id_richiesto=None):
        self.id = id
        self.data_ora = data_ora
        self.stato = stato
        self.id_richiedente = id_richiedente
        self.id_richiesto = id_richiesto


    # metodo di deserializzazione
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione
    def serializzazione(self):
        return self.__dict__
