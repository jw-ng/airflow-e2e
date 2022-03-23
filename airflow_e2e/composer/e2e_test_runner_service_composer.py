from pathlib import Path

from airflow_e2e.composer.docker_compose_file.docker_compose_tests_yaml_file import DockerComposeTestsYamlFile

DOCKER_COMPOSE_TESTS_YML_FILE_NAME = "docker-compose-tests.yml"


class E2eTestRunnerServiceComposer:
    def __init__(self, dags: str, tests: str):
        self.yaml_file = DockerComposeTestsYamlFile(
            dags_folder=dags,
            tests_folder=tests,
        )

    def with_custom_test_packages(self) -> "E2eTestRunnerServiceComposer":
        self.yaml_file = self.yaml_file.with_custom_test_packages()
        return self

    def setup(self, working_dir: Path):
        output_file_path = working_dir / DOCKER_COMPOSE_TESTS_YML_FILE_NAME
        with output_file_path.open(mode="w") as output_file:
            output_file.write(self.yaml_file.content)
