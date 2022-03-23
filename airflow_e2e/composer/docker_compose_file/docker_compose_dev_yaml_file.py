import typing

import yaml

from airflow_e2e.composer.docker_compose_file.docker_compose_version import (
    DOCKER_COMPOSE_VERSION,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_seeder_service import AirflowSeederService


class DockerComposeDevYamlFile:
    def __init__(self):
        self._version = DOCKER_COMPOSE_VERSION
        self._services = {"airflow-scheduler": AirflowSeederService().data}

    @property
    def data(self) -> typing.Dict:
        return self._version if len(self._services) == 0 else {
            **self._version,
            **{"services": self._services},
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)
