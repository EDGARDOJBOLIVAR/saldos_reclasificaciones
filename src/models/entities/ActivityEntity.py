from .BaseEntity import BaseEntity

class Activity(BaseEntity):
    def __init__(self, id, nombre = '') -> None:
        self.id = id
        self.nombre = nombre