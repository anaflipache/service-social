# 📲 Service Social

**Service Social** è un'applicazione web che funge da back-end per un social network. Sviluppata in Python, si interfaccia con un database **MySQL** per fornire dati in formato **JSON** tramite API.


## 💡 Funzionalità implementate

L'applicazione fornisce tre endpoint principali:

### 🔹 Endpoint #1 – Elenco utenti registrati

`GET /utenti`

Restituisce per ogni utente:

- `id`
- `data_registrazione` 
- `nome`, `cognome`, `email`, `nickname`, `password`
- `post`: elenco dei post dell'utente con:
  - `id`, `data_pubblicazione` 
  - `contenuto`
  - `numero_like`

---

### 🔹 Endpoint #2 – Elenco dei post

`GET /post`

Restituisce per ogni post:

- `id`
- `data_pubblicazione` 
- `nickname` dell'utente
- `commenti`: elenco con:
  - `id`, `data_pubblicazione` 
  - `contenuto`
  - `nickname` del commentatore

---

### 🔹 Endpoint #3 – Dati utente per nickname

`GET /utenti/{nickname}`

Restituisce per l'utente identificato:

- `id`
- `data_registrazione` 
- `nome`, `cognome`, `email`
- `commenti`: elenco con:
  - `id`, `data_pubblicazione` 
  - `contenuto`
  - `id_post` a cui il commento si riferisce

---

## 📌 Tecnologie utilizzate

- **Python**: backend
- **Flask** – framework per la creazione dell’API 
- **MySQL** – database relazionale
- **JSON** – formato di scambio dati

## 🔒 Licenza

Distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

