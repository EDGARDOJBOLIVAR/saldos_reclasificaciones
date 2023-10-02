from abc import ABC

class BaseEntity(ABC):
    id = None

    def to_dict(self):
        return vars(self)