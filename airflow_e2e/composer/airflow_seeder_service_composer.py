from pathlib import Path

import yaml

from airflow_e2e.composer import copy_from_template
from airflow_e2e.composer.constants import (
    TEMPLATES_DIR_PATH,
)
from airflow_e2e.composer.docker_compose_file.docker_compose_dev_yaml_file import (
    DockerComposeDevYamlFile,
)
from airflow_e2e.composer.seeder_file.connections_yaml_file import ConnectionsYamlFile

DOCKER_COMPOSE_DEV_YML_FILE_NAME = "docker-compose-dev.yml"

AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME = (
    "airflow-connections-and-variables-seeder"
)

CONNECTIONS_YML_TEMPLATE_FILE_NAME = "connections.yml.template"
CONNECTIONS_YML_FILE_NAME = "connections.yml"

VARIABLES_JSON_TEMPLATE_FILE_NAME = "variables.json.template"
VARIABLES_JSON_FILE_NAME = "variables.json"

SEEDER_TEMPLATE_MAP = {
    VARIABLES_JSON_TEMPLATE_FILE_NAME: VARIABLES_JSON_FILE_NAME,
}


class AirflowSeederServiceComposer:
    def setup(self, working_dir: Path):
        docker_compose_dev_yaml_file = DockerComposeDevYamlFile()
        output_file_path = working_dir / DOCKER_COMPOSE_DEV_YML_FILE_NAME
        with output_file_path.open(mode="w") as f:
            f.write(docker_compose_dev_yaml_file.content)

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

        connections_example_yaml_file = ConnectionsYamlFile()
        connections_yaml_file_path = (
            airflow_connections_and_variables_seeder_folder_path
            / CONNECTIONS_YML_FILE_NAME
        )
        with connections_yaml_file_path.open(mode="w") as f:
            f.write(yaml.safe_dump(connections_example_yaml_file.data))

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
