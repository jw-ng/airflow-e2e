import json
import tempfile
from pathlib import Path

from airflow_e2e.composer.airflow_seeder_service_composer import AirflowSeederServiceComposer


class TestAirflowSeederServiceComposer:
    def test_should_create_docker_compose_dev_yml_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_dev_yml_file_path = Path(temp_dir) / "docker-compose-dev.yml"
            assert docker_compose_dev_yml_file_path.exists()

    def test_should_setup_correct_dags_folder_in_docker_compose_dev_yml_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_dev_yml_file_path = Path(temp_dir) / "docker-compose-dev.yml"

            with docker_compose_dev_yml_file_path.open() as f:
                actual = f.read()

            expected_docker_compose_dev_yml_file_path = (
                Path(__file__).resolve().parent.parent
                / "resources"
                / "expected_docker-compose-dev.yml"
            )
            with expected_docker_compose_dev_yml_file_path.open() as f:
                expected = f.read()

            assert actual == expected

    def test_should_create_airflow_connections_and_variable_seeder_folder_in_docker_base_folder(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            expected_seeder_folder_path = (
                Path(temp_dir) / "airflow-connections-and-variables-seeder"
            )

            assert expected_seeder_folder_path.exists()

    def test_should_create_connections_seeder_yml_file_in_airflow_connections_and_variables_seeder_folder(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            connections_seeder_yml_file = (
                Path(temp_dir)
                / "airflow-connections-and-variables-seeder"
                / "connections.yml"
            )

            assert connections_seeder_yml_file.exists()

    def test_should_write_some_example_connections_in_connections_seeder_yml_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            connections_seeder_yml_file = (
                Path(temp_dir)
                / "airflow-connections-and-variables-seeder"
                / "connections.yml"
            )

            with connections_seeder_yml_file.open() as f:
                actual = f.readlines()

            assert actual == [
                "example_conn_id:\n",
                "  conn_type: mongo\n",
                "  host: 192.168.1.123\n",
                "  port: 27017\n",
            ]

    def test_should_create_variables_json_file_in_airflow_connections_and_variables_seeder_folder(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            variables_json_file = (
                Path(temp_dir)
                / "airflow-connections-and-variables-seeder"
                / "variables.json"
            )

            assert variables_json_file.exists()

    def test_should_write_some_example_variables_in_variables_json_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            variables_json_file = (
                Path(temp_dir)
                / "airflow-connections-and-variables-seeder"
                / "variables.json"
            )

            with variables_json_file.open() as f:
                actual = json.load(f)

            assert actual == {
                "example_string_variable": "example_string_value",
                "example_json_variable": {"foo": "bar", "baz": 42},
                "example_array_variable": ["lorem", "ipsum"],
            }
