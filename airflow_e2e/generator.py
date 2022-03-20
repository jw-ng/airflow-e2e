import typing
from pathlib import Path
from string import Template

DOCKER_FOLDER_NAME = "docker"

REPO_ROOT_DIR_PATH = Path(__file__).resolve().parent.parent
TEMPLATES_FOLDER_NAME = "templates"

DAGS_FOLDER_TEMPLATE_STRING = "DAGS_FOLDER"
TESTS_FOLDER_TEMPLATE_STRING = "TESTS_FOLDER"

DOCKER_COMPOSE_YML_FILE_NAME = "docker-compose.yml"
DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME = f"{DOCKER_COMPOSE_YML_FILE_NAME}.template"

DOCKER_COMPOSE_TESTS_YML_FILE_NAME = "docker-compose-tests.yml"
DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_TESTS_YML_FILE_NAME}.template"
)

DOCKER_COMPOSE_DEV_YML_FILE_NAME = "docker-compose-dev.yml"
DOCKER_COMPOSE_DEV_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_DEV_YML_FILE_NAME}.template"
)

TEMPLATE_MAP = {
    DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME: DOCKER_COMPOSE_YML_FILE_NAME,
    DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME: DOCKER_COMPOSE_TESTS_YML_FILE_NAME,
    DOCKER_COMPOSE_DEV_YML_TEMPLATE_FILE_NAME: DOCKER_COMPOSE_DEV_YML_FILE_NAME,
}

AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME = (
    "airflow-connections-and-variables-seeder"
)

CONNECTIONS_YML_TEMPLATE_FILE_NAME = "connections.yml.template"
CONNECTIONS_YML_FILE_NAME = "connections.yml"

VARIABLES_JSON_TEMPLATE_FILE_NAME = "variables.json.template"
VARIABLES_JSON_FILE_NAME = "variables.json"


def generate(dags: str, tests: str, working_dir: str):
    substitutions = {
        DAGS_FOLDER_TEMPLATE_STRING: dags,
        TESTS_FOLDER_TEMPLATE_STRING: tests,
    }

    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME
    docker_folder_path.mkdir(parents=True)

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


def _setup_docker_compose_file(
    template_file_name: str,
    output_file_name: str,
    docker_folder_path: Path,
    substitutions: typing.Dict[str, str],
):
    docker_compose_yml_template_file_path = (
        REPO_ROOT_DIR_PATH / TEMPLATES_FOLDER_NAME / template_file_name
    )
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
    airflow_connections_and_variables_seeder_folder_path.mkdir(parents=True)

    seeder_template_map = {
        CONNECTIONS_YML_TEMPLATE_FILE_NAME: CONNECTIONS_YML_FILE_NAME,
        VARIABLES_JSON_TEMPLATE_FILE_NAME: VARIABLES_JSON_FILE_NAME,
    }

    for template_file_name, output_file_name in seeder_template_map.items():
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
            REPO_ROOT_DIR_PATH
            / TEMPLATES_FOLDER_NAME
            / AIRFLOW_CONNECTIONS_AND_VARIABLES_SEEDER_FOLDER_NAME
            / template_file_name
    )
    with seeder_template_file_path.open(mode="r") as template_file:
        template = template_file.read()

    output_file_path = seeder_base_folder_path / output_file_name
    with output_file_path.open(mode="w") as f:
        f.write(template)
