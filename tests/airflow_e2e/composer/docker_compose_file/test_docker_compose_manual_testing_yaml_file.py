from unittest.mock import call

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

    def test_content_should_contain_correct_yaml_content(self, mocker):

        mock_yaml_safe_dump = mocker.patch(
            "airflow_e2e.composer.docker_compose_file.docker_compose_manual_testing_yaml_file.yaml.safe_dump"
        )

        yaml_file = DockerComposeManualTestingYamlFile()
        _ = yaml_file.content

        assert mock_yaml_safe_dump.call_count == 1
        assert mock_yaml_safe_dump.call_args == call(yaml_file.data, sort_keys=False)
