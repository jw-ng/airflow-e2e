from airflow_e2e.composer.docker_compose_file.services.airflow_redis_service import (
    AirflowRedisService,
)


class TestAirflowRedisService:
    def test_should_return_correct_airflow_redis_service_settings(self):
        assert AirflowRedisService().data == {
            "container_name": "airflow-redis",
            "image": "bitnami/redis:latest",
            "environment": ["ALLOW_EMPTY_PASSWORD=yes"],
        }
