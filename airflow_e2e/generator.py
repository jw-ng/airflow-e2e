from pathlib import Path

DOCKER_FOLDER_NAME = "docker"

REPO_ROOT_DIR_PATH = Path(__file__).resolve().parent.parent
TEMPLATES_FOLDER_NAME = "templates"

DOCKER_COMPOSE_YML_FILE_NAME = "docker-compose.yml"
DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME = f"{DOCKER_COMPOSE_YML_FILE_NAME}.template"


def generate(
    dags: str,
    working_dir: str,
):
    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME

    docker_folder_path.mkdir(parents=True)

    template_yml_file_path = (
        REPO_ROOT_DIR_PATH
        / TEMPLATES_FOLDER_NAME
        / DOCKER_COMPOSE_YML_TEMPLATE_FILE_NAME
    )
    with template_yml_file_path.open(mode="r") as template_file:
        template = template_file.read()

    docker_compose_yml_file_path = docker_folder_path / DOCKER_COMPOSE_YML_FILE_NAME
    with docker_compose_yml_file_path.open("w") as docker_compose_yml_file:
        docker_compose_yml_file.write(template.replace("{{ DAGS_FOLDER }}", dags))
