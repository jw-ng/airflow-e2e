import tempfile
from pathlib import Path

from airflow_e2e.generator.airflow_core_services_composer import (
    AirflowCoreServicesComposer,
)


class TestAirflowCoreServicesComposer:
    def test_should_create_docker_compose_yml_file_in_specified_working_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_yml_file_path = Path(temp_dir) / "docker-compose.yml"
            assert docker_compose_yml_file_path.exists()

    def test_should_setup_correct_dags_folder_in_docker_compose_yml_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_yml_file_path = Path(temp_dir) / "docker-compose.yml"
            with docker_compose_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker_compose.yml"
            )
            with expected_docker_compose_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected

    def test_should_omit_requirements_txt_mount_in_docker_compose_yml_file_when_not_needed(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup_without_mount(working_dir=Path(temp_dir))

            docker_compose_yml_file_path = (
                Path(temp_dir) / "docker-compose.yml"
            )
            with docker_compose_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose_without_requirements.yml"
            )
            with expected_docker_compose_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected
