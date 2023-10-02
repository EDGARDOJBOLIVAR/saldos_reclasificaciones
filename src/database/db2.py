from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, DatabaseError
from decouple import config

class Database2:
    __engine = None
    _last_error = ''
    _string_conection = ''

    def __init__(self):
        driver=config('DB_TYPE2', default='SIN_ASIGNAR')
        host=config(f"{driver}_HOST")
        port=config(f"{driver}_PORT")
        user=config(f"{driver}_USER")
        password=config(f"{driver}_PW")
        db=config(f"{driver}_DB")

        if driver == "PGSQL2":
            cadena_conexion = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        else:
            raise ValueError("Driver de base de datos no compatible")
        
        self._string_conection = cadena_conexion
        self.__engine = create_engine(cadena_conexion, execution_options={"autocommit": True})

    def test(self):
        try:
            with self.__engine.connect():
                return True
        except (OperationalError, DatabaseError)as ex:
            self._last_error = f"Error conexión: {ex.args[0]}"
            return False

    def execute(self, query: str, params: dict = None):
        query = query.strip()
        try:
            with self.__engine.connect() as conexion:
                if params != None:
                    return conexion.execute(text(query), params)
                else:
                    return conexion.execute(text(query))
        except (OperationalError, DatabaseError) as ex:
            self._last_error = f"Error: {ex.args[0]}"
            raise ex
    
    def getAll(self, query: str, params: dict = None):
        cursor = self.execute(query, params)
        columns = self._getColumns(cursor)
        all_rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return all_rows
    
    def getOne(self, query: str, params: dict = None):
        cursor = self.execute(query, params)
        columns = self._getColumns(cursor)
        row = cursor.fetchone()
        if row is not None: 
            row = dict(zip(columns, row))
        return row

    def insert(self, query: str, params: dict = None, columnId='id') -> int:
        query = f"{query} RETURNING {columnId}"
        
        connection = self.__engine.connect()
        try:
            trans = connection.begin()

            # Ejecuta la consulta de inserción con RETURNING
            if params != None:
                result = connection.execute(text(query), params)
            else:
                result = connection.execute(text(query))

            # Obtiene el ID del registro insertado
            inserted_id = result.fetchone()[0]

            # Confirma la transacción
            trans.commit()

            return inserted_id
        except Exception as e:
            # Si ocurre un error, revierte la transacción
            trans.rollback()
            raise e
        finally:
            # Cierra la conexión
            connection.close()

    
    def _getColumns(self, cursor):
        return [col.lower() for col in cursor.keys()]
    
    # def get_conection(self):
    #     return self.__engine.connect()
    
    @property
    def last_error(self):
        return self._last_error
    
    @property
    def string_conection(self):
        return self._string_conection
    
BD2 = Database2()