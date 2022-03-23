from pathlib import Path

from airflow_e2e.composer.docker_compose_file.docker_compose_manual_testing_yaml_file import \
    DockerComposeManualTestingYamlFile

DOCKER_COMPOSE_MANUAL_TESTING_YML_FILE_NAME = "docker-compose-manual-testing.yml"


class ManualE2eTestRunnerServiceComposer:
    def setup(self, working_dir: Path):
        yaml_file = DockerComposeManualTestingYamlFile()
        output_file_path = working_dir / DOCKER_COMPOSE_MANUAL_TESTING_YML_FILE_NAME
        with output_file_path.open(mode="w") as output_file:
            output_file.write(yaml_file.content)
