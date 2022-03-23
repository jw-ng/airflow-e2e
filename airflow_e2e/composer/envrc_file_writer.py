from pathlib import Path

from airflow_e2e.composer.constants import TEMPLATES_DIR_PATH


ENVRC_TEMPLATE_FILE_NAME = ".envrc.template"
ENVRC_FILE_NAME = ".envrc"


class EnvrcFileWriter:
    def setup(self, working_dir: Path):
        template_file_path = TEMPLATES_DIR_PATH / ENVRC_TEMPLATE_FILE_NAME

        with template_file_path.open(mode="r") as template_file:
            template = template_file.read()

        output_file_path = working_dir / ENVRC_FILE_NAME
        with output_file_path.open(mode="w") as f:
            f.write(template)
