import typing

import yaml

from airflow_e2e.composer.docker_compose_file.constants import (
    AIRFLOW_SCHEDULER_SERVICE_NAME,
    AIRFLOW_WEB_SERVICE_NAME,
    AIRFLOW_WORKER_SERVICE_NAME,
    POSTGRESQL_SERVICE_NAME,
    REDIS_SERVICE_NAME,
    SERVICES,
    VERSION,
    VERSION_3_7,
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


class DockerComposeYamlFile:
    def __init__(self, dags_folder: str):
        self._services = {
            AIRFLOW_WEB_SERVICE_NAME: AirflowWebService(),
            AIRFLOW_SCHEDULER_SERVICE_NAME: AirflowSchedulerService(
                dags_folder=dags_folder
            ),
            AIRFLOW_WORKER_SERVICE_NAME: AirflowWorkerService(dags_folder=dags_folder),
            POSTGRESQL_SERVICE_NAME: AirflowPostgresqlService(),
            REDIS_SERVICE_NAME: AirflowRedisService(),
        }

    @property
    def data(self) -> typing.Dict:
        return {
            VERSION: VERSION_3_7,
            SERVICES: {
                service_name: service.data
                for service_name, service in self._services.items()
            },
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)

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
