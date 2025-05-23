import pymysql

class Repository:

    # connessione al database
    @staticmethod
    def _get_connection():
        return pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="esercizio_service_social"
        )


    # manipolazione dati (DML)
    def manipolazione(self, sql, valori):
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, valori)
                    connection.commit()
                    return cursor.rowcount
        except Exception as e:
            print(e)
            return "Errore Database"


    # dati singolo
    def recupero_singolo(self, sql, valori):
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, valori)
                    return cursor.fetchone()
        except Exception as e:
            print(e)
            return "Errore Database"


    # dati multiplo
    def recupero_multiplo(self, sql, valori=None):
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    if valori:
                        cursor.execute(sql, valori)
                    else:
                        cursor.execute(sql)
                    return cursor.fetchall()
        except Exception as e:
            print(e)
            return "Errore Database"
