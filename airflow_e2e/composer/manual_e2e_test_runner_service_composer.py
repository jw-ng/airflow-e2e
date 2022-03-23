from pathlib import Path

from airflow_e2e.composer import copy_from_template
from airflow_e2e.composer.constants import TEMPLATES_DIR_PATH

DOCKER_COMPOSE_MANUAL_TESTING_YML_FILE_NAME = "docker-compose-manual-testing.yml"
DOCKER_COMPOSE_MANUAL_TESTING_YML_TEMPLATE_FILE_NAME = (
    f"{DOCKER_COMPOSE_MANUAL_TESTING_YML_FILE_NAME}.template"
)


class ManualE2eTestRunnerServiceComposer:
    def setup(self, working_dir: Path):
        template_file_path = (
            TEMPLATES_DIR_PATH / DOCKER_COMPOSE_MANUAL_TESTING_YML_TEMPLATE_FILE_NAME
        )
        output_file_path = working_dir / DOCKER_COMPOSE_MANUAL_TESTING_YML_FILE_NAME

        copy_from_template(
            template_file_path=template_file_path,
            output_file_path=output_file_path,
        )
