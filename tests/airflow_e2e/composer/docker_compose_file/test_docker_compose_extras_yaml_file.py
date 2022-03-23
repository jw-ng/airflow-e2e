from unittest.mock import call

import pytest as pytest

from airflow_e2e.composer.docker_compose_file.docker_compose_extras_yaml_file import (
    DockerComposeExtrasYamlFile,
)
from airflow_e2e.composer.docker_compose_file.services.mongodb_extra_service import (
    MONGODB_EXTRA_SERVICE,
)


class TestDockerComposeExtrasYamlFile:
    def test_data_should_contain_version(self):
        yaml_file = DockerComposeExtrasYamlFile()

        assert yaml_file.data.get("version") == "3.7"

    def test_data_should_return_only_mongod_service_when_with_mongo(self):
        yaml_file = DockerComposeExtrasYamlFile().with_mongo()

        assert yaml_file.data.get("services") == MONGODB_EXTRA_SERVICE

    @pytest.mark.parametrize(
        "yaml_file",
        (DockerComposeExtrasYamlFile(), DockerComposeExtrasYamlFile().with_mongo()),
    )
    def test_content_should_return_correct_yaml_content(
        self, mocker, yaml_file: DockerComposeExtrasYamlFile
    ):
        mock_yaml_safe_dump = mocker.patch(
            "airflow_e2e.composer.docker_compose_file.docker_compose_extras_yaml_file.yaml.safe_dump"
        )

        _ = yaml_file.content

        assert mock_yaml_safe_dump.call_count == 1
        assert mock_yaml_safe_dump.call_args == call(yaml_file.data, sort_keys=False)
