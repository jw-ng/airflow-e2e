from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)
from airflow_e2e.composer.docker_compose_file.constants import TEST_RUNNER_SERVICE_NAME
from airflow_e2e.composer.docker_compose_file.services.manual_e2e_test_runner_service import (
    ManualE2eTestRunnerService,
)


class DockerComposeManualTestingYamlFile(BaseDockerComposeYamlFile):
    def __init__(self):
        super().__init__()

        self._services = {TEST_RUNNER_SERVICE_NAME: ManualE2eTestRunnerService()}
