import typing

import yaml

from airflow_e2e.composer.docker_compose_file.docker_compose_version import (
    DOCKER_COMPOSE_VERSION,
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
        self._version = DOCKER_COMPOSE_VERSION
        self._services = {
            "airflow-web": AirflowWebService(),
            "airflow-scheduler": AirflowSchedulerService(dags_folder=dags_folder),
            "airflow-worker": AirflowWorkerService(dags_folder=dags_folder),
            "postgresql": AirflowPostgresqlService(),
            "redis": AirflowRedisService(),
        }

    @property
    def data(self) -> typing.Dict:
        return {
            **self._version,
            **{
                "services": {
                    service_name: service.data
                    for service_name, service in self._services.items()
                }
            },
        }

    @property
    def content(self) -> str:
        return yaml.safe_dump(self.data, sort_keys=False)

    def with_custom_airflow_packages(self) -> "DockerComposeYamlFile":
        airflow_web_service = self._services.get("airflow-web")
        airflow_scheduler_service = self._services.get("airflow-scheduler")
        airflow_worker_service = self._services.get("airflow-worker")

        self._services = {
            **self._services,
            **{
                "airflow-web": airflow_web_service.with_custom_airflow_packages(),
                "airflow-scheduler": airflow_scheduler_service.with_custom_airflow_packages(),
                "airflow-worker": airflow_worker_service.with_custom_airflow_packages(),
            }
        }

        return self
