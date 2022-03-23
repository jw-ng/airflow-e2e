import typing

from airflow_e2e.composer.docker_compose_file.services.base_service import BaseService


class AirflowWorkerService(BaseService):
    def __init__(self, dags_folder: str):
        self._data = {
            "container_name": "airflow-worker",
            "image": "bitnami/airflow-worker:latest",
            "depends_on": [
                "airflow-web",
            ],
            "volumes": [
                f"../{dags_folder}:/opt/bitnami/airflow/dags",
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

    def with_custom_airflow_packages(self) -> "AirflowWorkerService":
        volumes = self._data.get("volumes").copy()
        volumes += ["../requirements.txt:/bitnami/python/requirements.txt"]
        self._data["volumes"] = volumes

        return self

    @property
    def data(self) -> typing.Dict:
        return {"airflow-worker": self._data}
