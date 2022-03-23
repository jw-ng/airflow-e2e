import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, mock_open

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
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        spy_yaml_file = mocker.patch(
            "airflow_e2e.composer.extra_services_composer.DockerComposeExtrasYamlFile",
            return_value=mock_yaml_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.extra_services_composer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer()

            composer.setup(working_dir=Path(temp_dir))

            assert spy_yaml_file.call_count == 1
            assert spy_yaml_file.call_args == call()

    def test_setup_should_write_to_output_with_correct_content(self, mocker):
        mock_yaml_file_instance = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.extra_services_composer.DockerComposeExtrasYamlFile",
            return_value=mock_yaml_file_instance,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.extra_services_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer()

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert output_file_handle.write.call_count == 1
            assert output_file_handle.write.call_args == call(
                mock_yaml_file_instance.content
            )

    def test_setup_should_setup_correct_docker_compose_extras_yml_file_when_with_mongo(
        self, mocker
    ):
        mock_yaml_file_instance = MagicMock()
        mock_yaml_file_with_mongo_instance = MagicMock()
        mock_yaml_file_instance.with_mongo.return_value = (
            mock_yaml_file_with_mongo_instance
        )
        mocker.patch(
            "airflow_e2e.composer.extra_services_composer.DockerComposeExtrasYamlFile",
            return_value=mock_yaml_file_instance,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.extra_services_composer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            composer = ExtraServicesComposer().with_mongodb()

            composer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert output_file_handle.write.call_count == 1
            assert output_file_handle.write.call_args == call(
                mock_yaml_file_with_mongo_instance.content
            )
