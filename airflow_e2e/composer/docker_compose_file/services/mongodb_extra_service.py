import typing


class MongoDbExtraService:
    def __init__(self):
        self._data = {
            "container_name": "airflow-mongodb",
            "image": "mongo:latest",
            "command": "mongod",
            "ports": ["27017:27017"],
        }

    @property
    def data(self) -> typing.Dict:
        return {"mongodb": self._data}
