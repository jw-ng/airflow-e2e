import typing
from pathlib import Path
from string import Template

from airflow_e2e.generator import copy_from_template
from airflow_e2e.generator.constants import (
    DAGS_FOLDER_TEMPLATE_STRING,
    TEMPLATES_DIR_PATH,
)

DOCKER_COMPOSE_YML_FILE_NAME = "docker-compose.yml"
DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME = f"{DOCKER_COMPOSE_YML_FILE_NAME}.template"
DOCKER_COMPOSE_YML_WITHOUT_REQUIREMENTS_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_YML_FILE_NAME}_without_requirements.template"
)


class AirflowCoreServicesComposer:
    def __init__(self, dags: str):
        self.substitutions = {DAGS_FOLDER_TEMPLATE_STRING: dags}

    def setup(self, working_dir: Path):
        template_file_path = TEMPLATES_DIR_PATH / DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME
        output_file_path = working_dir / DOCKER_COMPOSE_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )

    def setup_without_mount(self, working_dir: Path):
        template_file_path = (
            TEMPLATES_DIR_PATH
            / DOCKER_COMPOSE_YML_WITHOUT_REQUIREMENTS_TEMPLATE_FILE_NAME
        )
        output_file_path = working_dir / DOCKER_COMPOSE_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )
