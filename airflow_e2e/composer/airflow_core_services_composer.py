from pathlib import Path

from airflow_e2e.composer.docker_compose_file.docker_compose_yaml_file import DockerComposeYamlFile

DOCKER_COMPOSE_YML_FILE_NAME = "docker-compose.yml"


class AirflowCoreServicesComposer:
    def __init__(self, dags: str):
        self.yaml_file = DockerComposeYamlFile(dags_folder=dags)

    def with_custom_airflow_packages(self) -> "AirflowCoreServicesComposer":
        self.yaml_file = self.yaml_file.with_custom_airflow_packages()
        return self

    def setup(self, working_dir: Path):
        output_file_path = working_dir / DOCKER_COMPOSE_YML_FILE_NAME
        with output_file_path.open(mode="w") as output_file:
            output_file.write(self.yaml_file.content)
