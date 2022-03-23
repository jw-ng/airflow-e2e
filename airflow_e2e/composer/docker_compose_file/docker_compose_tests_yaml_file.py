from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)
from airflow_e2e.composer.docker_compose_file.constants import TEST_RUNNER_SERVICE_NAME
from airflow_e2e.composer.docker_compose_file.services.e2e_test_runner_service import (
    E2eTestRunnerService,
)


class DockerComposeTestsYamlFile(BaseDockerComposeYamlFile):
    def __init__(self, dags_folder: str, tests_folder: str):
        super().__init__()

        self._services = {
            TEST_RUNNER_SERVICE_NAME: E2eTestRunnerService(
                dags_folder=dags_folder,
                tests_folder=tests_folder,
            ),
        }

    def with_custom_test_packages(self) -> "DockerComposeTestsYamlFile":
        e2e_test_runner_service = self._services.get(TEST_RUNNER_SERVICE_NAME)

        self._services = {
            **self._services,
            **{
                TEST_RUNNER_SERVICE_NAME: e2e_test_runner_service.with_custom_test_packages()
            },
        }

        return self
