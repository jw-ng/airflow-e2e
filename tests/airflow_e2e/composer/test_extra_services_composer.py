import tempfile
from pathlib import Path

from airflow_e2e.composer.extra_services_composer import ExtraServicesComposer


class TestExtraServicesComposer:
    def test_setup_should_create_docker_compose_extras_yml_file_in_specified_working_directory(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_extras_yml_file_path = (
                Path(temp_dir) / "docker-compose-extras.yml"
            )
            assert docker_compose_extras_yml_file_path.exists()

    def test_setup_should_setup_correct_docker_compose_extras_yml_file_when_no_extra_services_specified(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_extras_yml_file_path = (
                Path(temp_dir) / "docker-compose-extras.yml"
            )
            with docker_compose_extras_yml_file_path.open(mode="r") as f:
                actual = f.read()

            expected_docker_compose_extras_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-extras_with_no_services.yml"
            )
            with expected_docker_compose_extras_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected

    def test_setup_should_setup_correct_docker_compose_extras_yml_file_when_with_mongo(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer().with_mongodb()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_extras_yml_file_path = (
                Path(temp_dir) / "docker-compose-extras.yml"
            )
            with docker_compose_extras_yml_file_path.open(mode="r") as f:
                actual = f.read()

            expected_docker_compose_extras_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-extras_with_only_mongo.yml"
            )
            with expected_docker_compose_extras_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected
