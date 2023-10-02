from models.entities.AuditTaskImplEntity import AuditTaskImpl
from .BaseModel import BaseModel
from datetime import datetime

class CorteDatos2Model(BaseModel):
    _Table = 'corte_datos_2'

    def __init__(self) -> None:
        pass

    @classmethod
    def inserts(self, corte_id: int, datos: list[AuditTaskImpl]):
        for data in datos:
            query = f"""INSERT INTO {self._Table} (id, instancia_id, corte_id, actividad) values (DEFAULT, :instancia_id, :corte_id, :actividad)"""
        
            self.BD2.insert(
                query, 
                {
                    'instancia_id': data.processinstanceid, 
                    'corte_id': corte_id, 
                    'actividad': data.task
                }
            )

        return True