from model.post_pubblicati import PostPubblicati
from model.commenti import Commenti
from model.utenti import Utente
from repository.repository import Repository


class PostService:

    def __init__(self):
        self.repository = Repository()


    def elenco_post(self):
        sql_post= ("SELECT post_pubblicati.id, post_pubblicati.data_ora, utenti.nickname FROM post_pubblicati JOIN utenti ON post_pubblicati.id_utente = utenti.id")
        ottenuto_db_post= self.repository.recupero_multiplo(sql_post)
        if isinstance(ottenuto_db_post, str):
            return {"codice": 500, "messaggio": ottenuto_db_post}, 500
        # Recupera i commenti e il nickname di chi li ha scritti
        sql_commenti= ("SELECT commenti.id, commenti.data_ora, commenti.contenuto, commenti.id_utente, commenti.id_post, utenti.nickname FROM commenti JOIN utenti ON commenti.id_utente = utenti.id")
        ottenuto_db_commenti = self.repository.recupero_multiplo(sql_commenti)
        if isinstance(ottenuto_db_commenti, str):
            return {"codice": 500, "messaggio": ottenuto_db_commenti}, 500

        posts=[]
        for record_post in ottenuto_db_post:
            # Crea il post con nickname come stringa, NON come oggetto Utente
            post=PostPubblicati(id=record_post[0], data_ora=record_post[1], nickname=record_post[2], commenti=[])
            for record_commento in ottenuto_db_commenti:
                if post.id == record_commento[4]:
                    commento = Commenti(id=record_commento[0], data_ora=record_commento[1], contenuto=record_commento[2], nickname=record_commento[5])
                    post.commenti.append(commento)
                posts.append(post)
        return [post_pubblicato.serializzazione_due() for post_pubblicato in posts], 200
