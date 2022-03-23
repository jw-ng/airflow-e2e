import typing

import yaml

from airflow_e2e.composer.docker_compose_file.docker_compose_version import (
    DOCKER_COMPOSE_VERSION,
)
from airflow_e2e.composer.docker_compose_file.services.e2e_test_runner_service import (
    E2eTestRunnerService,
)


class DockerComposeTestsYamlFile:
    def __init__(self, dags_folder: str, tests_folder: str):
        self._version = DOCKER_COMPOSE_VERSION
        self._services = {
            "test-runner": E2eTestRunnerService(
                dags_folder=dags_folder,
                tests_folder=tests_folder,
            ),
        }

    @property
    def data(self) -> typing.Dict:
        return {
            **self._version,
            **{
                "services": {
                    service_name: service.data
                    for service_name, service in self._services.items()
                }
            },
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)

    def with_custom_test_packages(self) -> "DockerComposeTestsYamlFile":
        e2e_test_runner_service = self._services.get("test-runner")

        self._services = {
            **self._services,
            **{"test-runner": e2e_test_runner_service.with_custom_test_packages()},
        }

        return self
