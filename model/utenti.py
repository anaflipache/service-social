class Utente:

    def __init__(self, id=None, data_iscrizione=None, nome=None, cognome=None, mail=None, nickname=None, password=None,
                 tipo_profilo=None, auth_token=None, post_pubblicati=None):
        self.id = id
        self.data_iscrizione = data_iscrizione
        self.nome = nome
        self.cognome = cognome
        self.mail = mail
        self.nickname = nickname
        self.password = password
        self.tipo_profilo = tipo_profilo
        self.auth_token = auth_token
        self.post_pubblicati = post_pubblicati if post_pubblicati else []


    # metodo di deserializzazione
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione
    def serializzazione(self):
        return {
            "id": self.id,
            "data_iscrizione": self.data_iscrizione,
            "nome": self.nome,
            "cognome": self.cognome,
            "mail": self.mail,
            "nickname": self.nickname,
            "password": self.password,
            "post_pubblicati": [post_pubblicati.serializzazione_per_utenti() for post_pubblicati in self.post_pubblicati]
        }
