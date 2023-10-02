from .BaseModel import BaseModel
from .entities.ActivityEntity import Activity

class ActivityModel(BaseModel):
    _Table = 'actividad'

    def __init__(self) -> None:
        pass

    @classmethod
    def get(self, id):
        Node = None
        query = f"""SELECT id, nombre 
        FROM {self._Table} TB 
        WHERE id = :id"""
        data = self.BD.getOne(query, {'id': id})
        if data != None:
            Node = Activity(id=data['id'], nombre=data['nombre'])

        return Node

    @classmethod
    def getAll(self, code):
        Nodes = []
        query = f"""SELECT id, nombre 
        FROM {self._Table} TB 
        ORDER BY id asc"""
        
        data = self.BD.getAll(query)
        
        if data != None:
            for row in data:
                node = Activity(id=row['id'], nombre=row['nombre'])
                Nodes.append(node)

        return Nodes