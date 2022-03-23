import os
import typing
from pathlib import Path
from string import Template

from airflow_e2e.generator.airflow_core_services_composer import (
    AirflowCoreServicesComposer,
)
from airflow_e2e.generator.airflow_seeder_service_composer import (
    AirflowSeederServiceComposer,
)
from airflow_e2e.generator.constants import (
    DAGS_FOLDER_TEMPLATE_STRING,
    DOCKER_FOLDER_NAME,
    ENVRC_FILE_NAME,
    ENVRC_TEMPLATE_FILE_NAME,
    TEMPLATES_DIR_PATH,
    TESTS_FOLDER_TEMPLATE_STRING,
)
from airflow_e2e.generator.e2e_test_runner_service_composer import (
    E2eTestRunnerServiceComposer,
)


from airflow_e2e.generator.manual_e2e_test_runner_service_composer import ManualE2eTestRunnerServiceComposer


def generate(dags: str, tests: str, working_dir: str = None):
    _generate(
        dags=dags,
        tests=tests,
        mount_requirements=True,
        working_dir=working_dir,
    )


def generate_without_requirements(dags: str, tests: str, working_dir: str = None):
    _generate(
        dags=dags,
        tests=tests,
        mount_requirements=False,
        working_dir=working_dir,
    )


def _generate(
    dags: str,
    tests: str,
    mount_requirements: bool,
    working_dir: str = None,
):
    substitutions = {
        DAGS_FOLDER_TEMPLATE_STRING: dags,
        TESTS_FOLDER_TEMPLATE_STRING: tests,
    }

    working_dir = os.getcwd() if working_dir is None else working_dir

    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME
    docker_folder_path.mkdir(parents=True, exist_ok=True)

    _setup_envrc_file(docker_folder_path)

    airflow_core_services_composer = AirflowCoreServicesComposer(dags=dags)
    if mount_requirements:
        airflow_core_services_composer.setup(working_dir=docker_folder_path)
    else:
        airflow_core_services_composer.setup_without_mount(
            working_dir=docker_folder_path
        )

    e2e_test_runner_service_composer = E2eTestRunnerServiceComposer(
        dags=dags, tests=tests
    )
    e2e_test_runner_service_composer.setup(working_dir=docker_folder_path)

    airflow_seeder_service_composer = AirflowSeederServiceComposer()
    airflow_seeder_service_composer.setup(working_dir=docker_folder_path)

    manual_e2e_test_runner_service_composer = ManualE2eTestRunnerServiceComposer()
    manual_e2e_test_runner_service_composer.setup(working_dir=docker_folder_path)


def _setup_envrc_file(docker_folder_path: Path):
    envrc_template_file_path = TEMPLATES_DIR_PATH / ENVRC_TEMPLATE_FILE_NAME

    with envrc_template_file_path.open(mode="r") as template_file:
        template = template_file.read()

    output_file_path = docker_folder_path / ENVRC_FILE_NAME
    with output_file_path.open(mode="w") as f:
        f.write(template)
