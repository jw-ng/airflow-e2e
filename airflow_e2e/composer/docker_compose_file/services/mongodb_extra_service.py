import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class MongoDbExtraService(BaseService):
    @property
    def data(self) -> typing.Dict:
        return {
            "container_name": "airflow-mongodb",
            "image": "mongo:latest",
            "command": "mongod",
            "ports": ["27017:27017"],
        }
