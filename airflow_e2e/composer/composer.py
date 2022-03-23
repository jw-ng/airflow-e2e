from pathlib import Path

from airflow_e2e.builder.builder import build_airflow_core_services_composer
from airflow_e2e.composer.airflow_seeder_service_composer import (
    AirflowSeederServiceComposer,
)
from airflow_e2e.composer.constants import DOCKER_FOLDER_NAME
from airflow_e2e.composer.e2e_test_runner_service_composer import (
    E2eTestRunnerServiceComposer,
)
from airflow_e2e.composer.envrc_file_writer import EnvrcFileWriter
from airflow_e2e.composer.manual_e2e_test_runner_service_composer import (
    ManualE2eTestRunnerServiceComposer,
)


def setup(
    dags: str,
    tests: str,
    working_dir: str,
    with_custom_airflow_packages: bool,
):
    docker_folder_path = Path(working_dir) / DOCKER_FOLDER_NAME
    docker_folder_path.mkdir(parents=True, exist_ok=True)

    airflow_core_services_composer = build_airflow_core_services_composer(
        dags=dags,
        with_custom_airflow_packages=with_custom_airflow_packages,
    )
    airflow_core_services_composer.setup(working_dir=docker_folder_path)

    e2e_test_runner_service_composer = E2eTestRunnerServiceComposer(
        dags=dags, tests=tests
    )
    e2e_test_runner_service_composer.setup(working_dir=docker_folder_path)

    airflow_seeder_service_composer = AirflowSeederServiceComposer()
    airflow_seeder_service_composer.setup(working_dir=docker_folder_path)

    manual_e2e_test_runner_service_composer = ManualE2eTestRunnerServiceComposer()
    manual_e2e_test_runner_service_composer.setup(working_dir=docker_folder_path)

    envrc_file_writer = EnvrcFileWriter()
    envrc_file_writer.setup(working_dir=docker_folder_path)
