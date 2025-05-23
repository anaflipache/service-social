from flask import Flask, request
from service.utenti_service import UtentiService
from service.post_service import PostService


# istanziazione applicazione web di tipo Flask
app = Flask(__name__)


# istanziazione componenti Service
utenti_service = UtentiService()
post_service = PostService()



#****************ENDPOINT****************#

# endpoint #1: elenco utenti
# localhost:5000/social/elenco_utenti/get
@app.get("/social/elenco_utenti/get")
def endpoint_elenco_utenti():
    return utenti_service.elenco_utenti()


# endpoint #2: elenco post
# localhost:5000/social/post/get
@app.get("/social/post/get")
def endpoint_elenco_post():
    return post_service.elenco_post()





# blocco condizionale di eseguibilità
if __name__ == "__main__":
    app.run()
