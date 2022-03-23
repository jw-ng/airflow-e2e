import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowWorkerService(BaseService):
    def __init__(self, dags_folder: str):
        self._volumes = [f"../{dags_folder}:/opt/bitnami/airflow/dags"]
        self._base_data = {
            "container_name": "airflow-worker",
            "image": "bitnami/airflow-worker:latest",
            "depends_on": [
                "airflow-web",
            ],
            "environment": [
                "PYTHONPATH=/opt/bitnami/airflow",
                "AIRFLOW_DATABASE_HOST=airflow-postgresql",
                "AIRFLOW_DATABASE_NAME=${AIRFLOW_DATABASE_NAME}",
                "AIRFLOW_DATABASE_USERNAME=${AIRFLOW_DATABASE_USERNAME}",
                "AIRFLOW_DATABASE_PASSWORD=${AIRFLOW_DATABASE_PASSWORD}",
                "AIRFLOW_EXECUTOR=CeleryExecutor",
                "AIRFLOW_FERNET_KEY=${AIRFLOW_FERNET_KEY}",
                "AIRFLOW_LOAD_EXAMPLES=no",
                "AIRFLOW_SECRET_KEY=${AIRFLOW_SECRET_KEY}",
                "AIRFLOW_WEBSERVER_HOST=airflow-web",
                "AIRFLOW__API__AUTH_BACKEND=airflow.api.auth.backend.basic_auth",
                "AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False",
            ],
        }

    @property
    def data(self) -> typing.Dict:
        return {**self._base_data, **{"volumes": self._volumes}}

    def with_custom_airflow_packages(self) -> "AirflowWorkerService":
        self._volumes += ["../requirements.txt:/bitnami/python/requirements.txt"]

        return self
