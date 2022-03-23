import tempfile
from pathlib import Path

from airflow_e2e.composer.e2e_test_runner_service_composer import (
    E2eTestRunnerServiceComposer,
)


class TestE2eTestRunnerServiceComposer:
    def test_should_create_docker_compose_tests_yml_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = E2eTestRunnerServiceComposer(
                dags="some/dags/folder",
                tests="some/tests/folder",
            )

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-tests.yml"
            )

            assert docker_compose_tests_yml_file_path.exists()

    def test_should_setup_correct_dags_folder_in_docker_compose_tests_yml_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = E2eTestRunnerServiceComposer(
                dags="some/dags/folder",
                tests="some/tests/folder",
            )

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-tests.yml"
            )

            with docker_compose_tests_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_tests_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-tests.yml"
            )
            with expected_docker_compose_tests_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected

    def test_setup_should_omit_requirements_dev_txt_mount_in_docker_compose_tests_yml_file_when_with_custom_test_packages(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = E2eTestRunnerServiceComposer(
                dags="some/dags/folder",
                tests="some/tests/folder",
            ).with_custom_test_packages()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_tests_yml_file_path = (
                Path(temp_dir) / "docker-compose-tests.yml"
            )
            with docker_compose_tests_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_tests_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-tests_without_requirements_dev.yml"
            )
            with expected_docker_compose_tests_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected
