import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call, mock_open

from airflow_e2e.composer.envrc_file_writer import EnvrcFileWriter


class TestEnvrcFileWriter:
    def test_should_create_envrc_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = EnvrcFileWriter()

            writer.setup(working_dir=Path(temp_dir))

            envrc_file_path = Path(temp_dir) / ".envrc"
            assert envrc_file_path.exists()

    def test_should_setup_correct_template_in_envrc_file(self, mocker):
        mock_envrc_file_instance = MagicMock()
        spy_envrc_file = mocker.patch(
            "airflow_e2e.composer.envrc_file_writer.EnvrcFile",
            return_value=mock_envrc_file_instance,
        )
        mocker.patch(
            "airflow_e2e.composer.envrc_file_writer.Path.open",
            mock_open(),
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            writer = EnvrcFileWriter()

            writer.setup(working_dir=Path(temp_dir))

            assert spy_envrc_file.call_count == 1
            assert spy_envrc_file.call_args == call()

    def test_should_write_to_output_with_correct_content(self, mocker):
        mock_envrc_file_instance = MagicMock()
        mocker.patch(
            "airflow_e2e.composer.envrc_file_writer.EnvrcFile",
            return_value=mock_envrc_file_instance,
        )

        mock_output_file_open = mock_open()
        mocker.patch(
            "airflow_e2e.composer.envrc_file_writer.Path.open",
            mock_output_file_open,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            writer = EnvrcFileWriter()

            writer.setup(working_dir=Path(temp_dir))

            output_file_handle = mock_output_file_open()
            assert output_file_handle.write.call_count == 1
            assert output_file_handle.write.call_args == call(
                mock_envrc_file_instance.content
            )
