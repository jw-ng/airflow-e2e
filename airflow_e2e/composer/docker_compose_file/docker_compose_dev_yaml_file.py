from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)
from airflow_e2e.composer.docker_compose_file.constants import (
    AIRFLOW_SCHEDULER_SERVICE_NAME,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_seeder_service import (
    AirflowSeederService,
)


class DockerComposeDevYamlFile(BaseDockerComposeYamlFile):
    def __init__(self):
        super().__init__()

        self._services = {AIRFLOW_SCHEDULER_SERVICE_NAME: AirflowSeederService()}
