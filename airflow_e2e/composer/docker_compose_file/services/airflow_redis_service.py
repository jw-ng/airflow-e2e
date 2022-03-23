import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowRedisService(BaseService):
    @property
    def data(self) -> typing.Dict:
        return {
            "container_name": "airflow-redis",
            "image": "bitnami/redis:latest",
            "environment": ["ALLOW_EMPTY_PASSWORD=yes"],
        }
