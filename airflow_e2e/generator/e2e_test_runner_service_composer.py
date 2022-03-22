import typing
from pathlib import Path
from string import Template

from airflow_e2e.generator import copy_from_template
from airflow_e2e.generator.constants import (
    DAGS_FOLDER_TEMPLATE_STRING,
    TEMPLATES_DIR_PATH,
    TESTS_FOLDER_TEMPLATE_STRING,
)


DOCKER_COMPOSE_TESTS_YML_FILE_NAME = "docker-compose-tests.yml"
DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_TESTS_YML_FILE_NAME}.template"
)


class E2eTestRunnerServiceComposer:
    def __init__(self, dags: str, tests: str):
        self.substitutions = {
            DAGS_FOLDER_TEMPLATE_STRING: dags,
            TESTS_FOLDER_TEMPLATE_STRING: tests,
        }

    def setup(self, working_dir: Path):
        template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME
        )
        output_file_path = working_dir / DOCKER_COMPOSE_TESTS_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )

    def setup_without_mount(self, working_dir: Path):
        template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_TESTS_YML_TEMPLATE_FILE_NAME
        )
        output_file_path = working_dir / DOCKER_COMPOSE_TESTS_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
            substitutions=self.substitutions,
        )
