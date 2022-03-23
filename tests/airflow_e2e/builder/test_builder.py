from pathlib import Path

from airflow_e2e.builder.builder import build_airflow_core_services_composer, build_e2e_test_runner_service_composer
from airflow_e2e.composer.constants import TEMPLATES_DIR_PATH


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_without_custom_mount_when_with_custom_airflow_packages_is_false():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_packages=False
    )

    assert (
        composer.template_file_path
        == Path(TEMPLATES_DIR_PATH) / "docker-compose.yml.template"
    )


def test_build_airflow_core_services_composer_should_return_airflow_core_services_composer_with_custom_airflow_packages_when_with_custom_mount_is_true():
    composer = build_airflow_core_services_composer(
        dags="some/dags/folder", with_custom_airflow_packages=True
    )

    assert (
        composer.template_file_path
        == Path(TEMPLATES_DIR_PATH) / "docker-compose.yml_without_requirements.template"
    )


def test_build_e2e_test_runner_service_composer_should_return_e2e_test_runner_service_composer_without_custom_installation_when_with_custom_test_packages_is_false():
    composer = build_e2e_test_runner_service_composer(
        dags="some/dags/folder",
        tests="some/tests/folder",
        with_custom_test_packages=False,
    )

    assert (
            composer.template_file_path
            == Path(TEMPLATES_DIR_PATH) / "docker-compose-tests.yml.template"
    )


def test_build_e2e_test_runner_service_composer_should_return_e2e_test_runner_service_composer_with_custom_installation_when_with_custom_test_packages_is_true():
    composer = build_e2e_test_runner_service_composer(
        dags="some/dags/folder",
        tests="some/tests/folder",
        with_custom_test_packages=True,
    )

    assert (
            composer.template_file_path
            == Path(TEMPLATES_DIR_PATH) / "docker-compose-tests.yml_without_requirements_dev.template"
    )
