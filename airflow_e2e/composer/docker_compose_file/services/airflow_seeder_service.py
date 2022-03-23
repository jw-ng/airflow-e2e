import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowSeederService(BaseService):
    @property
    def data(self) -> typing.Dict:
        return {
            "volumes": ["./airflow-connections-and-variables-seeder/:/tmp/seed/"],
        }
