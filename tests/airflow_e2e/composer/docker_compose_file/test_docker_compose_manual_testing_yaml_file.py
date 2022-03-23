from airflow_e2e.composer.docker_compose_file.docker_compose_manual_testing_yaml_file import (
    DockerComposeManualTestingYamlFile,
)
from airflow_e2e.composer.docker_compose_file.services.manual_e2e_test_runner_service import (
    ManualE2eTestRunnerService,
)


class TestDockerComposeManualTestingYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeManualTestingYamlFile()

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_contain_e2e_test_runner_service(self):
        yaml_file = DockerComposeManualTestingYamlFile()

        service = ManualE2eTestRunnerService()

        assert yaml_file.data.get("services").get("test-runner") == service.data
