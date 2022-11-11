from BaseModel import BaseModel
from device.device import Device

import uuid
import sqlite3


class DeviceModel(BaseModel):
    def __init__(self):
        super().__init__()

    def createTable(self) -> None:
        query = """
        CREATE TABLE IF NOT EXISTS devices (
              id TEXT UNIQUE,
              name TEXT UNIQUE,
              hostname TEXT UNIQUE,
              port INTEGER
        );
        """
        self.cursor.execute(query)

    def getOne(self) -> Device:
        pass

    def getAll(self):
        query = """
        SELECT id,name,hostname,port FROM devices
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        print(result)

    def insert(self, name: str, hostname: str, port: int) -> dict:
        deviceId = uuid.uuid4()

        query = """
        INSERT OR IGNORE INTO devices(
            id,
            name,
            hostname,
            port
            ) 
        VALUES(?,?,?,?)
        RETURNING *;
        """

        try:
            self.cursor.execute(query, (deviceId.hex, name, hostname, port))
            result = self.cursor.fetchone()
            self.conn.commit()
        except sqlite3.Error as err:
            raise Exception("Device could not be inserted: " + str(err))

        return Device(result[0], result[1], result[2], result[3]).__dict__ if result != None else {"Error": "Device already exists"}

    def delete(self):
        pass


dm = DeviceModel()
print(dm.insert('Test1', '0.0.0.0', 55443))
