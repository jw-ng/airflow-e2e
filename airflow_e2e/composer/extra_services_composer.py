from pathlib import Path

from airflow_e2e.composer.docker_compose_file.docker_compose_extras_yaml_file import DockerComposeExtrasYamlFile

DOCKER_COMPOSE_EXTRAS_YAML_FILE_NAME = "docker-compose-extras.yml"


class ExtraServicesComposer:
    def __init__(self):
        self.yaml_file = DockerComposeExtrasYamlFile()

    def with_mongodb(self) -> "ExtraServicesComposer":
        self.yaml_file.with_mongo()
        return self

    def setup(self, working_dir: Path):
        output_file_path = working_dir / DOCKER_COMPOSE_EXTRAS_YAML_FILE_NAME
        with output_file_path.open(mode="w") as f:
            f.write(self.yaml_file.content)
