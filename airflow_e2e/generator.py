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


def generate(
    dags: str,
    tests: str,
    working_dir: str,
):
    substitutions = {
        DAGS_FOLDER_TEMPLATE_STRING: dags,
        TESTS_FOLDER_TEMPLATE_STRING: tests,
    }

    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME

    docker_folder_path.mkdir(parents=True)

    docker_compose_yml_template_file_path = (
        REPO_ROOT_DIR_PATH
        / TEMPLATES_FOLDER_NAME
        / DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME
    )
    with docker_compose_yml_template_file_path.open(mode="r") as template_file:
        docker_compose_yml_template = Template(template_file.read())

    docker_compose_yml_file_path = docker_folder_path / DOCKER_COMPOSE_YML_FILE_NAME
    with docker_compose_yml_file_path.open("w") as docker_compose_yml_file:
        content = docker_compose_yml_template.substitute(**substitutions)
        docker_compose_yml_file.write(content)

    docker_compose_tests_yml_template_file_path = (
        REPO_ROOT_DIR_PATH
        / TEMPLATES_FOLDER_NAME
        / DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME
    )
    with docker_compose_tests_yml_template_file_path.open(mode="r") as template_file:
        docker_compose_tests_yml_template = Template(template_file.read())

    docker_compose_tests_yml_file_name = (
        docker_folder_path / DOCKER_COMPOSE_TESTS_YML_FILE_NAME
    )
    with docker_compose_tests_yml_file_name.open("w") as docker_compose_tests_yml_file:
        content = docker_compose_tests_yml_template.substitute(**substitutions)
        docker_compose_tests_yml_file.write(content)
