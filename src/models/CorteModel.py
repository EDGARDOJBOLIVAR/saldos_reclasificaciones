from .BaseModel import BaseModel
from datetime import datetime
import pytz

class CorteModel(BaseModel):
    _Table = 'corte'

    def __init__(self) -> None:
        pass

    @classmethod
    def insert(self):
        bogota_tz = pytz.timezone('America/Bogota')
        fecha_hora_actual = datetime.now(bogota_tz)
        fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

        query = f"""INSERT INTO {self._Table} (id, fecha) values (DEFAULT, :date)"""
        
        inserted = self.BD2.insert(query, {'date': fecha_hora_formateada})

        return inserted