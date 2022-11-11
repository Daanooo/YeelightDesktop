import sqlite3
from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self):
        self.dbName = 'data.db'
        self.conn = sqlite3.connect(self.dbName, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        self.createTable()

    @abstractmethod
    def createTable(self) -> None:
        pass

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getOne(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass
