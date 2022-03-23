import typing

import yaml

from airflow_e2e.composer.docker_compose_file.docker_compose_version import (
    DOCKER_COMPOSE_VERSION,
)
from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import MONGODB_EXTRA_SERVICE


class DockerComposeExtrasYamlFile:
    def __init__(self):
        self._version = DOCKER_COMPOSE_VERSION
        self._services = {}

    @property
    def data(self) -> typing.Dict:
        return self._version if len(self._services) == 0 else {
            **self._version,
            **{"services": self._services},
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)

    def with_mongo(self) -> "DockerComposeExtrasYamlFile":
        services = self._services.get("services", {})

        self._services = {
            **services,
            **MONGODB_EXTRA_SERVICE,
        }
        return self
