import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, mock_open

from airflow_e2e.composer.manual_e2e_test_runner_service_composer import (
    ManualE2eTestRunnerServiceComposer,
)


class TestManualE2eTestRunnerServiceComposer:
    def test_should_create_docker_compose_manual_testing_yml_file_in_docker_base_folder(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ManualE2eTestRunnerServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-manual-testing.yml"
            )

            assert docker_compose_tests_yml_file_path.exists()

    def test_should_setup_correct_docker_compose_manual_testing_yml_file(self, mocker):
        mock_yaml_file_instance = MagicMock()
        spy_yaml_file = mocker.patch(
            "airflow_e2e.composer.manual_e2e_test_runner_service_composer.DockerComposeManualTestingYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.manual_e2e_test_runner_service_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ManualE2eTestRunnerServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            assert spy_yaml_file.call_count == 1
            assert spy_yaml_file.call_args == call()
