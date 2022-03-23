from pathlib import Path

from airflow_e2e.composer import copy_from_template
from airflow_e2e.composer.constants import (
    TEMPLATES_DIR_PATH,
)

DOCKER_COMPOSE_DEV_YML_FILE_NAME = "docker-compose-dev.yml"
DOCKER_COMPOSE_DEV_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_DEV_YML_FILE_NAME}.template"
)

AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME = (
    "airflow-connections-and-variables-seeder"
)

CONNECTIONS_YML_TEMPLATE_FILE_NAME = "connections.yml.template"
CONNECTIONS_YML_FILE_NAME = "connections.yml"

VARIABLES_JSON_TEMPLATE_FILE_NAME = "variables.json.template"
VARIABLES_JSON_FILE_NAME = "variables.json"

SEEDER_TEMPLATE_MAP = {
    CONNECTIONS_YML_TEMPLATE_FILE_NAME: CONNECTIONS_YML_FILE_NAME,
    VARIABLES_JSON_TEMPLATE_FILE_NAME: VARIABLES_JSON_FILE_NAME,
}


class AirflowSeederServiceComposer:
    def setup(self, working_dir: Path):
        template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_DEV_YML_TEMPLATE_FILE_NAME
        )
        output_file_path = working_dir / DOCKER_COMPOSE_DEV_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
        )

        self._setup_airflow_connections_and_variables_seeder_folder(
            working_dir=working_dir
        )

    def _setup_airflow_connections_and_variables_seeder_folder(self, working_dir: Path):
        airflow_connections_and_variables_seeder_folder_path = (
            working_dir / AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME
        )
        airflow_connections_and_variables_seeder_folder_path.mkdir(
            parents=True, exist_ok=True
        )

        for template_file_name, output_file_name in SEEDER_TEMPLATE_MAP.items():
            template_file_path = (
                TEMPLATES_DIR_PATH
                / AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME
                / template_file_name
            )
            copy_from_template(
                template_file_path=template_file_path,
                output_file_path=(
                    airflow_connections_and_variables_seeder_folder_path
                    / output_file_name
                ),
            )
