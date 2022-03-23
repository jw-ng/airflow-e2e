from airflow_e2e.composer.docker_compose_file.services.airflow_web_service import (
    AirflowWebService,
)


class TestAirflowWebService:
    def test_should_return_correct_airflow_web_service_settings(self):
        service = AirflowWebService()

        assert service.data == {
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

    def test_should_return_airflow_web_service_with_requirements_txt_mount_when_with_custom_airflow_packages(
        self,
    ):
        service = AirflowWebService().with_custom_airflow_packages()

        assert service.data == {
            "container_name": "airflow-web",
            "image": "bitnami/airflow:latest",
            "depends_on": [
                "mongodb",
                "postgresql",
                "redis",
            ],
            "volumes": ["../requirements.txt:/bitnami/python/requirements.txt"],
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
