import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class MongoDbExtraService(BaseService):
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
