from pathlib import Path

from airflow_e2e.composer import copy_from_template
from airflow_e2e.composer.constants import (
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
        self.template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME
        )

    def with_custom_airflow_packages(self) -> "AirflowCoreServicesComposer":
        self.template_file_path = (
            TEMPLATES_DIR_PATH
            / DOCKER_COMPOSE_YML_WITHOUT_REQUIREMENTS_TEMPLATE_FILE_NAME
        )
        return self

    def setup(self, working_dir: Path):
        output_file_path = working_dir / DOCKER_COMPOSE_YML_FILE_NAME

        copy_from_template(
            template_file_path=self.template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )
