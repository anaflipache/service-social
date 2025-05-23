from model.utenti import Utente
from repository.repository import Repository
from model.post_pubblicati import PostPubblicati


class UtentiService:

    def __init__(self):
        self.repository = Repository()


    def elenco_utenti(self):
        sql_utenti= "SELECT * FROM utenti"
        ottenuto_db_utenti= self.repository.recupero_multiplo(sql_utenti)
        if isinstance(ottenuto_db_utenti, str):
            return {"codice": 500, "messaggio": ottenuto_db_utenti}, 500
        sql_post=("SELECT post_pubblicati.id, post_pubblicati.data_ora, post_pubblicati.contenuto, post_pubblicati.id_utente, COUNT(like_apposti.id) as 'numero_like' FROM post_pubblicati LEFT JOIN like_apposti ON post_pubblicati.id = like_apposti.id_post GROUP BY post_pubblicati.id")
        ottenuto_db_post = self.repository.recupero_multiplo(sql_post)
        if isinstance(ottenuto_db_post, str):
            return {"codice": 500, "messaggio": ottenuto_db_post}, 500

        utenti=[]
        for record_utente in ottenuto_db_utenti:
            utente=Utente(id=record_utente[0], data_iscrizione=record_utente[1], nome=record_utente[2],
                          cognome=record_utente[3], mail=record_utente[4], nickname=record_utente[5],
                          password=record_utente[6],post_pubblicati=[])
            for record_post in ottenuto_db_post:
                if utente.id == record_post[3]:
                    post_pubblicati=PostPubblicati(id=record_post[0],data_ora=record_post[1],
                    contenuto=record_post[2],numero_like=record_post[4])
                    utente.post_pubblicati.append(post_pubblicati)
                utenti.append(utente)
            return [utente.serializzazione() for utente in utenti], 200