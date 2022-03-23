from pathlib import Path

from airflow_e2e.composer.envrc_file import EnvrcFile

ENVRC_FILE_NAME = ".envrc"


class EnvrcFileWriter:
    def setup(self, working_dir: Path):
        file = EnvrcFile()

        output_file_path = working_dir / ENVRC_FILE_NAME
        with output_file_path.open(mode="w") as output_file:
            output_file.write(file.content)
