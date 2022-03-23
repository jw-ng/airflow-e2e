import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, mock_open

from airflow_e2e.composer.airflow_core_services_composer import (
    AirflowCoreServicesComposer,
)


class TestAirflowCoreServicesComposer:
    def test_setup_should_create_docker_compose_yml_file_in_specified_working_directory(
        self,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup(working_dir=Path(temp_dir))

            docker_compose_yml_file_path = Path(temp_dir) / "docker-compose.yml"
            assert docker_compose_yml_file_path.exists()

    def test_setup_should_setup_correct_dags_folder_in_docker_compose_yml_file(
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        spy_yaml_file = mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.DockerComposeYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup(working_dir=Path(temp_dir))

            assert spy_yaml_file.call_count == 1
            assert spy_yaml_file.call_args == call(dags_folder="some/dags/folder")

    def test_setup_should_write_to_output_with_correct_content(self, mocker):
        mock_yaml_file_instance = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.DockerComposeYamlFile",
            return_value=mock_yaml_file_instance,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(dags="some/dags/folder")

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert output_file_handle.write.call_count == 1
            assert output_file_handle.write.call_args == call(
                mock_yaml_file_instance.content
            )

    def test_setup_should_mount_requirements_txt_in_docker_compose_yml_file_when_with_custom_airflow_packages(
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        mock_yaml_file_with_custom_airflow_packages_instance = MagicMock()
        mock_yaml_file_instance.with_custom_airflow_packages.return_value = (
            mock_yaml_file_with_custom_airflow_packages_instance
        )
        mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.DockerComposeYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.airflow_core_services_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = AirflowCoreServicesComposer(
                dags="some/dags/folder"
            ).with_custom_airflow_packages()

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert output_file_handle.write.call_count == 1
            assert output_file_handle.write.call_args == call(
                mock_yaml_file_with_custom_airflow_packages_instance.content
            )
