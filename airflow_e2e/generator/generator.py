import os
import typing
from pathlib import Path
from string import Template

from airflow_e2e.generator.constants import (
    AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME,
    DAGS_FOLDER_TEMPLATE_STRING,
    DOCKER_FOLDER_NAME,
    ENVRC_FILE_NAME,
    ENVRC_TEMPLATE_FILE_NAME,
    SEEDER_TEMPLATE_MAP,
    TEMPLATES_DIR_PATH,
    TEMPLATE_MAP,
    TESTS_FOLDER_TEMPLATE_STRING,
)


def generate(dags: str, tests: str, working_dir: str = None):
    substitutions = {
        DAGS_FOLDER_TEMPLATE_STRING: dags,
        TESTS_FOLDER_TEMPLATE_STRING: tests,
    }

    working_dir = os.getcwd() if working_dir is None else working_dir

    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME
    docker_folder_path.mkdir(parents=True, exist_ok=True)

    for template_file_name, output_file_name in TEMPLATE_MAP.items():
        _setup_docker_compose_file(
            template_file_name=template_file_name,
            output_file_name=output_file_name,
            docker_folder_path=docker_folder_path,
            substitutions=substitutions,
        )

    _setup_airflow_connections_and_variables_seeder_folder(
        docker_folder_path=docker_folder_path
    )

    _setup_envrc_file(docker_folder_path)


def _setup_docker_compose_file(
    template_file_name: str,
    output_file_name: str,
    docker_folder_path: Path,
    substitutions: typing.Dict[str, str],
):
    docker_compose_yml_template_file_path = TEMPLATES_DIR_PATH / template_file_name
    with docker_compose_yml_template_file_path.open(mode="r") as template_file:
        docker_compose_yml_template = Template(template_file.read())

    docker_compose_yml_file_path = docker_folder_path / output_file_name
    with docker_compose_yml_file_path.open("w") as docker_compose_yml_file:
        content = docker_compose_yml_template.substitute(**substitutions)
        docker_compose_yml_file.write(content)


def _setup_airflow_connections_and_variables_seeder_folder(docker_folder_path: Path):
    airflow_connections_and_variables_seeder_folder_path = (
        docker_folder_path / AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME
    )
    airflow_connections_and_variables_seeder_folder_path.mkdir(
        parents=True, exist_ok=True
    )

    for template_file_name, output_file_name in SEEDER_TEMPLATE_MAP.items():
        _create_seeder_template_file(
            template_file_name=template_file_name,
            output_file_name=output_file_name,
            seeder_base_folder_path=airflow_connections_and_variables_seeder_folder_path,
        )


def _create_seeder_template_file(
    template_file_name: str,
    output_file_name: str,
    seeder_base_folder_path: Path,
):
    seeder_template_file_path = (
        TEMPLATES_DIR_PATH
        / AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME
        / template_file_name
    )
    with seeder_template_file_path.open(mode="r") as template_file:
        template = template_file.read()

    output_file_path = seeder_base_folder_path / output_file_name
    with output_file_path.open(mode="w") as f:
        f.write(template)


def _setup_envrc_file(docker_folder_path: Path):
    envrc_template_file_path = TEMPLATES_DIR_PATH / ENVRC_TEMPLATE_FILE_NAME

    with envrc_template_file_path.open(mode="r") as template_file:
        template = template_file.read()

    output_file_path = docker_folder_path / ENVRC_FILE_NAME
    with output_file_path.open(mode="w") as f:
        f.write(template)
