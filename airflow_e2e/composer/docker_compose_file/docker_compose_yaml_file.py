from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)
from airflow_e2e.composer.docker_compose_file.constants import (
    AIRFLOW_SCHEDULER_SERVICE_NAME,
    AIRFLOW_WEB_SERVICE_NAME,
    AIRFLOW_WORKER_SERVICE_NAME,
    POSTGRESQL_SERVICE_NAME,
    REDIS_SERVICE_NAME,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_postgresql_service import (
    AirflowPostgresqlService,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_redis_service import (
    AirflowRedisService,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_scheduler_service import (
    AirflowSchedulerService,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_web_service import (
    AirflowWebService,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_worker_service import (
    AirflowWorkerService,
)


class DockerComposeYamlFile(BaseDockerComposeYamlFile):
    def __init__(self, dags_folder: str):
        super().__init__()

        self._services = {
            AIRFLOW_WEB_SERVICE_NAME: AirflowWebService(),
            AIRFLOW_SCHEDULER_SERVICE_NAME: AirflowSchedulerService(
                dags_folder=dags_folder
            ),
            AIRFLOW_WORKER_SERVICE_NAME: AirflowWorkerService(dags_folder=dags_folder),
            POSTGRESQL_SERVICE_NAME: AirflowPostgresqlService(),
            REDIS_SERVICE_NAME: AirflowRedisService(),
        }

    def with_custom_airflow_packages(self) -> "DockerComposeYamlFile":
        airflow_web_service = self._services.get(AIRFLOW_WEB_SERVICE_NAME)
        airflow_scheduler_service = self._services.get(AIRFLOW_SCHEDULER_SERVICE_NAME)
        airflow_worker_service = self._services.get(AIRFLOW_WORKER_SERVICE_NAME)

        self._services = {
            **self._services,
            **{
                AIRFLOW_WEB_SERVICE_NAME: airflow_web_service.with_custom_airflow_packages(),
                AIRFLOW_SCHEDULER_SERVICE_NAME: airflow_scheduler_service.with_custom_airflow_packages(),
                AIRFLOW_WORKER_SERVICE_NAME: airflow_worker_service.with_custom_airflow_packages(),
            },
        }

        return self
