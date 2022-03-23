from airflow_e2e.composer.docker_compose_file.docker_compose_extras_yaml_file import (
    DockerComposeExtrasYamlFile,
)
from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import (
    MongoDbExtraService,
)


class TestDockerComposeExtrasYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeExtrasYamlFile()

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_return_only_mongod_service_when_with_mongo(self):
        yaml_file = DockerComposeExtrasYamlFile().with_mongo()

        mongodb_extra_service = MongoDbExtraService()

        assert (
            yaml_file.data.get("services").get("mongodb") == mongodb_extra_service.data
        )
