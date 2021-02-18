import psycopg2

class Conexion:

    def __init__(self):
        self.__con = psycopg2.connect("dbname=alquiler_db user=postgres host=localhost password=dgtic123")

    def getConexion(self):
        return self.__con