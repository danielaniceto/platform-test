import pymysql
import pymysql.cursors

class ConexaoBD():
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            port=3306,
            database="bd_web_rota",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_connection(self):
        return self.connection
    
    def get_cursor(self, conn:pymysql.connect):
        return conn.cursor()
    
    def close_cursor(self, cursor):
        cursor.close()

    def select_user(self):
            conection_consulta_users = self.get_connection
            try:
                cursor_user = self.get_cursor(conection_consulta_users)
                cursor_user.execute("SELECT * FROM users WHERE senha, email = '{senha}, {email}';")
                _data = cursor_user.fetchall()
                self.commit(conection_consulta_users)
                self.close_cursor(cursor_user)
                conection_consulta_users.close()
                if isinstance(_data, str) or isinstance(_data, bytes):
                    return []
                if not bool(_data):
                    return []
                return _data
            
            except Exception as error:
                print(error)
                conection_consulta_users.close()
                return None

class isCoordenadas():
    def __init__(self):
        self.connection = ConexaoBD.get_connection(self)

    def select_coordenadas(self):
        connction_consulta_coordenadas = ConexaoBD.get_connection
        try:
            cursor_coordenadas = ConexaoBD.get_connection(connction_consulta_coordenadas)
            cursor_coordenadas.execute("SELECT * FROM positions")
            _data = cursor_coordenadas.fetchall()
            self.commit(connction_consulta_coordenadas)
            self.close_cursor(cursor_coordenadas)
            connction_consulta_coordenadas.close()
            if isinstance(_data. str) or isinstance(_data, bytes):
                return[]
            if not bool(_data):
                    return []
            return _data
        
        except Exception as error:
            print(error)
            connction_consulta_coordenadas.close()
            return None
            