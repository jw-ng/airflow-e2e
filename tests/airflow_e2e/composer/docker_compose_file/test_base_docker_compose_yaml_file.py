from unittest.mock import call

from airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file import (
    BaseDockerComposeYamlFile,
)


class TestBaseDockerComposeYamlFile:
    def test_content_should_contain_correct_yaml_content(self, mocker):
        mock_yaml_safe_dump = mocker.patch(
            "airflow_e2e.composer.docker_compose_file.base_docker_compose_yaml_file.yaml.safe_dump"
        )

        yaml_file = BaseDockerComposeYamlFile()
        _ = yaml_file.content

        assert mock_yaml_safe_dump.call_count == 1
        assert mock_yaml_safe_dump.call_args == call(yaml_file.data, sort_keys=False)
