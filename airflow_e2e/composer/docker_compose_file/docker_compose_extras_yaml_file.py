from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)
from airflow_e2e.composer.docker_compose_file.constants import (
    MONGODB_SERVICE_NAME,
    SERVICES,
)
from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import (
    MongoDbExtraService,
)


class DockerComposeExtrasYamlFile(BaseDockerComposeYamlFile):
    def with_mongo(self) -> "DockerComposeExtrasYamlFile":
        services = self._services.get(SERVICES, {})

        mongodb_service = MongoDbExtraService()
        self._services = {
            **services,
            **{MONGODB_SERVICE_NAME: mongodb_service},
        }
        return self
