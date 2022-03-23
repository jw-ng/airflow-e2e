import tempfile
from pathlib import Path

from airflow_e2e.composer.manual_e2e_test_runner_service_composer import ManualE2eTestRunnerServiceComposer


class TestManualE2eTestRunnerServiceComposer:
    def test_should_create_docker_compose_tests_yml_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ManualE2eTestRunnerServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-manual-testing.yml"
            )

            assert docker_compose_tests_yml_file_path.exists()

    def test_should_setup_correct_dags_folder_in_docker_compose_tests_yml_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ManualE2eTestRunnerServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-manual-testing.yml"
            )

            with docker_compose_tests_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_tests_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-manual-testing.yml"
            )
            with expected_docker_compose_tests_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected
