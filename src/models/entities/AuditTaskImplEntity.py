from .BaseEntity import BaseEntity

class AuditTaskImpl(BaseEntity):
    def __init__(self, id, processinstanceid, task='') -> None:
        self.id = id
        self.processinstanceid = processinstanceid
        self.task = task