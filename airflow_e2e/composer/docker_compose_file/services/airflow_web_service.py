import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowWebService(BaseService):
    def __init__(self):
        self._volumes = []
        self._base_data = {
            "container_name": "airflow-web",
            "image": "bitnami/airflow:latest",
            "depends_on": [
                "mongodb",
                "postgresql",
                "redis",
            ],
            "environment": [
                "PYTHONPATH=/opt/bitnami/airflow",
                "AIRFLOW_HOME=/opt/bitnami/airflow",
                "AIRFLOW_EMAIL=${AIRFLOW_EMAIL}",
                "AIRFLOW_USERNAME=${AIRFLOW_USERNAME}",
                "AIRFLOW_PASSWORD=${AIRFLOW_PASSWORD}",
                "AIRFLOW_DATABASE_HOST=airflow-postgresql",
                "AIRFLOW_DATABASE_NAME=${AIRFLOW_DATABASE_NAME}",
                "AIRFLOW_DATABASE_USERNAME=${AIRFLOW_DATABASE_USERNAME}",
                "AIRFLOW_DATABASE_PASSWORD=${AIRFLOW_DATABASE_PASSWORD}",
                "AIRFLOW_EXECUTOR=CeleryExecutor",
                "AIRFLOW_FERNET_KEY=${AIRFLOW_FERNET_KEY}",
                "AIRFLOW_LOAD_EXAMPLES=no",
                "AIRFLOW_SECRET_KEY=${AIRFLOW_SECRET_KEY}",
                "AIRFLOW__API__AUTH_BACKEND=airflow.api.auth.backend.basic_auth",
                "AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False",
            ],
            "ports": ["8080:8080"],
            "healthcheck": {
                "test": ["CMD", "curl", "-f", "http://localhost:8080/health"],
                "interval": "10s",
                "timeout": "10s",
                "retries": 15,
            },
        }

    @property
    def data(self) -> typing.Dict:
        return (
            {**self._base_data, **{"volumes": self._volumes}}
            if self._volumes
            else self._base_data
        )

    def with_custom_airflow_packages(self) -> "AirflowWebService":
        self._volumes += ["../requirements.txt:/bitnami/python/requirements.txt"]
        return self
