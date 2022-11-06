from BaseModel import BaseModel


class DeviceModel(BaseModel):
    def __init__(self):
        super().__init__()

    def createTable(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS devices (
              id UUID,
              name TEXT,
              hostname TEXT,
              port INTEGER
        );
        """
        self.cursor.execute(query)

    def getOne(self):
        pass
    
    def getAll(self):
        pass
    
    def insert(self):
        pass
    
    def delete(self):
        pass

dm = DeviceModel()
