from airflow_e2e.composer.docker_compose_file.services.airflow_worker_service import (
    AirflowWorkerService,
)


class TestAirflowWorkerService:
    def test_should_return_correct_airflow_worker_service_settings(self):
        service = AirflowWorkerService(dags_folder="some/dags/folder")

        assert service.data == {
            "container_name": "airflow-worker",
            "image": "bitnami/airflow-worker:latest",
            "depends_on": [
                "airflow-web",
            ],
            "volumes": [
                "../some/dags/folder:/opt/bitnami/airflow/dags",
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

    def test_should_return_airflow_worker_service_with_requirements_txt_mount_when_with_custom_airflow_packages(
        self,
    ):
        service = AirflowWorkerService(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()

        assert service.data == {
            "container_name": "airflow-worker",
            "image": "bitnami/airflow-worker:latest",
            "depends_on": [
                "airflow-web",
            ],
            "volumes": [
                "../some/dags/folder:/opt/bitnami/airflow/dags",
                "../requirements.txt:/bitnami/python/requirements.txt",
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
