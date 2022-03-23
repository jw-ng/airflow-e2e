import typing

import yaml

from airflow_e2e.composer.docker_compose_file.docker_compose_version import (
    DOCKER_COMPOSE_VERSION,
)
from airflow_e2e.composer.docker_compose_file.services.manual_e2e_test_runner_service import ManualE2eTestRunnerService


class DockerComposeManualTestingYamlFile:
    def __init__(self):
        self._version = DOCKER_COMPOSE_VERSION
        self._services = {"test-runner": ManualE2eTestRunnerService().data}

    @property
    def data(self) -> typing.Dict:
        return {
            **self._version,
            **{
                "services": self._services
            },
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)
