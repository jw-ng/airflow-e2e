import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, mock_open

from airflow_e2e.composer.airflow_seeder_service_composer import (
    AirflowSeederServiceComposer,
)


class TestAirflowSeederServiceComposer:
    def test_should_create_docker_compose_dev_yml_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_dev_yml_file_path = Path(temp_dir) / "docker-compose-dev.yml"
            assert docker_compose_dev_yml_file_path.exists()

    def test_should_setup_correct_docker_compose_dev_yml_file(self, mocker):
        mock_yaml_file_instance = MagicMock()
        spy_yaml_file = mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.DockerComposeDevYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            assert spy_yaml_file.call_count == 1
            assert spy_yaml_file.call_args == call()

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

    def test_should_setup_correct_example_connections_in_connections_seeder_yml_file(
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        mock_yaml_file_instance.data = {}
        spy_yaml_file = mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.ConnectionsYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            assert spy_yaml_file.call_count == 1
            assert spy_yaml_file.call_args == call()

    def test_should_write_connections_seeder_yml_file_with_correct_content(
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.ConnectionsYamlFile",
            return_value=mock_yaml_file_instance,
        )

        mock_connections_yaml_file_content = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.yaml.safe_dump",
            return_value=mock_connections_yaml_file_content,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert (
                call(mock_connections_yaml_file_content)
                in output_file_handle.write.call_args_list
            )

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

    def test_should_setup_correct_example_variables_in_variables_json_file(
        self, mocker
    ):
        mock_json_file_instance = MagicMock()
        mock_json_file_instance.data = {}
        spy_json_file = mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.VariablesJsonFile",
            return_value=mock_json_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            assert spy_json_file.call_count == 1
            assert spy_json_file.call_args == call()


    def test_should_write_variables_json_file_with_correct_content(
        self, mocker
    ):
        mock_json_file_instance = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.VariablesJsonFile",
            return_value=mock_json_file_instance,
        )

        mock_variables_json_file_content = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.json.dumps",
            return_value=mock_variables_json_file_content,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.airflow_seeder_service_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowSeederServiceComposer()

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert (
                call(mock_variables_json_file_content)
                in output_file_handle.write.call_args_list
            )
