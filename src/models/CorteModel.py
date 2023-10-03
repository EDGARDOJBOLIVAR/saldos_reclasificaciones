from .BaseModel import BaseModel
from datetime import datetime

class CorteModel(BaseModel):
    _Table = 'corte'

    def __init__(self) -> None:
        pass

    @classmethod
    def insert(self):
        fecha_hora_actual = datetime.now()
        fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

        query = f"""INSERT INTO {self._Table} (id, fecha) values (DEFAULT, :date)"""
        
        inserted = self.BD2.insert(query, {'date': fecha_hora_formateada})

        return inserted