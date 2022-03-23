import typing

import yaml

from airflow_e2e.composer.docker_compose_file.constants import AIRFLOW_SCHEDULER_SERVICE_NAME, SERVICES, VERSION, \
    VERSION_3_7
from airflow_e2e.composer.docker_compose_file.services.airflow_seeder_service import AirflowSeederService


class DockerComposeDevYamlFile:
    def __init__(self):
        self._services = {AIRFLOW_SCHEDULER_SERVICE_NAME: AirflowSeederService().data}

    @property
    def data(self) -> typing.Dict:
        return (
            {VERSION: VERSION_3_7}
            if len(self._services) == 0
            else {
                VERSION: VERSION_3_7,
                SERVICES: self._services,
            }
        )

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)
