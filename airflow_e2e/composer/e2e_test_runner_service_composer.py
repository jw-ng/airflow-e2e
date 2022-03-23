from pathlib import Path

from airflow_e2e.composer import copy_from_template
from airflow_e2e.composer.constants import (
    DAGS_FOLDER_TEMPLATE_STRING,
    TEMPLATES_DIR_PATH,
    TESTS_FOLDER_TEMPLATE_STRING,
)

DOCKER_COMPOSE_TESTS_YML_FILE_NAME = "docker-compose-tests.yml"
DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_TESTS_YML_FILE_NAME}.template"
)
DOCKER_COMPOSE_TESTS_YML_WITHOUT_REQUIREMENTS_DEV_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_TESTS_YML_FILE_NAME}_without_requirements_dev.template"
)


class E2eTestRunnerServiceComposer:
    def __init__(self, dags: str, tests: str):
        self.substitutions = {
            DAGS_FOLDER_TEMPLATE_STRING: dags,
            TESTS_FOLDER_TEMPLATE_STRING: tests,
        }
        self.template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME
        )

    def with_custom_test_packages(self) -> "E2eTestRunnerServiceComposer":
        self.template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_TESTS_YML_WITHOUT_REQUIREMENTS_DEV_TEMPLATE_FILE_NAME
        )
        return self

    def setup(self, working_dir: Path):
        output_file_path = working_dir / DOCKER_COMPOSE_TESTS_YML_FILE_NAME

        copy_from_template(
            template_file_path=self.template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )
