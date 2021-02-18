from flask import current_app as app
from app.conexion.Conexion import Conexion

class SalaModel:
    """Clase SalaModel

    Esta clase gestiona registros de la tabla salas

    Autor: Juancito

    """

    def listarTodos(self):
        """listarTodos

        Obtiene todos los registros de salas

        """
        lista = []
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            querySQL = "SELECT * FROM referenciales.salas"
            cur.execute(querySQL)
            lista_salas = cur.fetchall()
            if len(lista_salas) > 0:
                for rs in lista_salas:
                    obj = {}
                    obj['id'] = rs[0]
                    obj['description'] = rs[1]
                    lista.append(obj)
        except con.Error as e:
            app.logger.error(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()
        return lista
        
