import tempfile
from pathlib import Path

from airflow_e2e.composer.envrc_file_writer import EnvrcFileWriter


class TestEnvrcFileWriter:
    def test_should_create_envrc_file_in_docker_base_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = EnvrcFileWriter()

            writer.setup(working_dir=Path(temp_dir))

            envrc_file_path = Path(temp_dir) / ".envrc"
            assert envrc_file_path.exists()

    def test_should_setup_correct_template_in_envrc_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = EnvrcFileWriter()

            writer.setup(working_dir=Path(temp_dir))

            envrc_file_path = Path(temp_dir) / ".envrc"
            with envrc_file_path.open() as f:
                actual = f.read()

            expected_envrc_file_path = (
                Path(__file__).resolve().parent.parent / "resources" / "expected_envrc"
            )
            with expected_envrc_file_path.open() as f:
                expected = f.read()

            assert actual == expected
