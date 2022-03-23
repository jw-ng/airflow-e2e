import typing
from abc import ABC

import yaml

from airflow_e2e.composer.docker_compose_file.constants import (
    SERVICES,
    VERSION,
    VERSION_3_7,
)


class BaseDockerComposeYamlFile(ABC):
    def __init__(self):
        self._services = {}

    @property
    def data(self) -> typing.Dict:
        return (
            {VERSION: VERSION_3_7}
            if len(self._services) == 0
            else {
                VERSION: VERSION_3_7,
                SERVICES: {
                    service_name: service.data
                    for service_name, service in self._services.items()
                },
            }
        )

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)
