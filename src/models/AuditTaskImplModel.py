from .BaseModel import BaseModel
from .entities.AuditTaskImplEntity import AuditTaskImpl

class AuditTaskImplModel(BaseModel):
    _Table = 'audittaskimpl'

    def __init__(self) -> None:
        pass

    @classmethod
    def getAll(self) -> list:
        Nodes = []
        query = f"""SELECT DISTINCT ON (processinstanceid) id, processinstanceid, name
        FROM {self._Table}
        WHERE deploymentid = 'EmpresaComunicaciones_1.0.2-SNAPSHOT' 
        ORDER BY processinstanceid, id desc"""
        
        data = self.BD.getAll(query)
        
        if data != None:
            for row in data:
                node = AuditTaskImpl(id=row['id'], processinstanceid=row['processinstanceid'], task=row['name'])
                Nodes.append(node)

        return Nodes