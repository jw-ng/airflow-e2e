from airflow_e2e.composer.docker_compose_file.docker_compose_dev_yaml_file import (
    DockerComposeDevYamlFile,
)
from airflow_e2e.composer.docker_compose_file.services.airflow_seeder_service import (
    AirflowSeederService,
)


class TestDockerComposeDevYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeDevYamlFile()

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_correct_seeder_service(self):
        yaml_file = DockerComposeDevYamlFile()

        service = AirflowSeederService()

        assert yaml_file.data.get("services").get("airflow-scheduler") == service.data
