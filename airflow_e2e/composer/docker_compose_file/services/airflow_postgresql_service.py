import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowPostgresqlService(BaseService):
    def __init__(self):
        self._data = {
            "container_name": "postgresql",
            "image": "bitnami/postgresql:latest",
            "environment": [
                "POSTGRESQL_DATABASE=${AIRFLOW_DATABASE_NAME}",
                "POSTGRESQL_USERNAME=${AIRFLOW_DATABASE_USERNAME}",
                "POSTGRESQL_PASSWORD=${AIRFLOW_DATABASE_PASSWORD}",
                "ALLOW_EMPTY_PASSWORD=yes",
            ],
            "ports": ["5432:5432"],
        }

    @property
    def data(self) -> typing.Dict:
        return {"postgresql": self._data}
