from airflow_e2e.composer.docker_compose_file.docker_compose_yaml_file import (
    DockerComposeYamlFile,
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


class TestDockerComposeYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_contain_airflow_web_service_without_requirements_txt_mount_by_default(
        self,
    ):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        service = AirflowWebService()

        assert yaml_file.data.get("services").get("airflow-web") == service.data

    def test_data_should_contain_airflow_web_service_with_requirements_txt_mount_when_specified(
        self,
    ):
        yaml_file = DockerComposeYamlFile(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()

        service = AirflowWebService().with_custom_airflow_packages()
        assert yaml_file.data.get("services").get("airflow-web") == service.data

    def test_data_should_contain_airflow_scheduler_service_without_requirements_txt_mount_by_default(
        self,
    ):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        service = AirflowSchedulerService(dags_folder="some/dags/folder")
        assert yaml_file.data.get("services").get("airflow-scheduler") == service.data

    def test_data_should_contain_airflow_scheduler_service_with_requirements_txt_mount_when_specified(
        self,
    ):
        yaml_file = DockerComposeYamlFile(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()

        service = AirflowSchedulerService(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()
        assert yaml_file.data.get("services").get("airflow-scheduler") == service.data

    def test_data_should_contain_airflow_worker_service_without_requirements_txt_mount_by_default(
        self,
    ):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        service = AirflowWorkerService(dags_folder="some/dags/folder")
        assert yaml_file.data.get("services").get("airflow-worker") == service.data

    def test_data_should_contain_airflow_worker_service_with_requirements_txt_mount_when_specified(
        self,
    ):
        yaml_file = DockerComposeYamlFile(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()

        service = AirflowWorkerService(
            dags_folder="some/dags/folder"
        ).with_custom_airflow_packages()
        assert yaml_file.data.get("services").get("airflow-worker") == service.data

    def test_data_should_contain_airflow_postgresql_service(self):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        service = AirflowPostgresqlService()
        assert yaml_file.data.get("services").get("postgresql") == service.data

    def test_data_should_contain_airflow_redis_service(self):
        yaml_file = DockerComposeYamlFile(dags_folder="some/dags/folder")

        service = AirflowRedisService()
        assert yaml_file.data.get("services").get("redis") == service.data
