import typing

import yaml

from airflow_e2e.composer.docker_compose_file.constants import SERVICES, TEST_RUNNER_SERVICE_NAME, VERSION, VERSION_3_7
from airflow_e2e.composer.docker_compose_file.services.manual_e2e_test_runner_service import (
    ManualE2eTestRunnerService,
)


class DockerComposeManualTestingYamlFile:
    def __init__(self):
        self._services = {TEST_RUNNER_SERVICE_NAME: ManualE2eTestRunnerService().data}

    @property
    def data(self) -> typing.Dict:
        return {VERSION: VERSION_3_7, SERVICES: self._services}

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)
