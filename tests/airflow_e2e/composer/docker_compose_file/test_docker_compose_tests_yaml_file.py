from airflow_e2e.composer.docker_compose_file.docker_compose_tests_yaml_file import (
    DockerComposeTestsYamlFile,
)
from airflow_e2e.composer.docker_compose_file.services.e2e_test_runner_service import (
    E2eTestRunnerService,
)


class TestDockerComposeTestsYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeTestsYamlFile(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        )

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_contain_e2e_test_runner_service_without_requirements_dev_txt_mount_by_default(
        self,
    ):
        yaml_file = DockerComposeTestsYamlFile(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        )

        service = E2eTestRunnerService(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        )

        assert yaml_file.data.get("services").get("test-runner") == service.data

    def test_data_should_contain_e2e_test_runner_service_with_requirements_dev_txt_mount_when_specified(
        self,
    ):
        yaml_file = DockerComposeTestsYamlFile(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        ).with_custom_test_packages()

        service = E2eTestRunnerService(
            dags_folder="some/dags/folder",
            tests_folder="some/tests/folder",
        ).with_custom_test_packages()
        assert yaml_file.data.get("services").get("test-runner") == service.data
