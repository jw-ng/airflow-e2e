import typing

import yaml

from airflow_e2e.composer.docker_compose_file.constants import (
    MONGODB_SERVICE_NAME,
    SERVICES,
    VERSION,
    VERSION_3_7,
)
from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import (
    MongoDbExtraService,
)


class DockerComposeExtrasYamlFile:
    def __init__(self):
        self._services = {}

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

    def with_mongo(self) -> "DockerComposeExtrasYamlFile":
        services = self._services.get(SERVICES, {})

        mongodb_service = MongoDbExtraService()
        self._services = {
            **services,
            **{MONGODB_SERVICE_NAME: mongodb_service.data},
        }
        return self
