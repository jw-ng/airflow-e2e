from airflow_e2e.composer.docker_compose_file.services.airflow_postgresql_service import (
    AirflowPostgresqlService,
)


class TestAirflowPostgresqlService:
    def test_should_return_correct_airflow_postgresql_service_settings(self):
        assert AirflowPostgresqlService().data == {
            "container_name": "airflow-postgresql",
            "image": "bitnami/postgresql:latest",
            "environment": [
                "POSTGRESQL_DATABASE=${AIRFLOW_DATABASE_NAME}",
                "POSTGRESQL_USERNAME=${AIRFLOW_DATABASE_USERNAME}",
                "POSTGRESQL_PASSWORD=${AIRFLOW_DATABASE_PASSWORD}",
                "ALLOW_EMPTY_PASSWORD=yes",
            ],
            "ports": ["5432:5432"],
        }
